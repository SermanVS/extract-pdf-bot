from asyncio import wait_for
from tg_bot import bot
from message_parser import MessageParser
from html_parser import HTMLParser
from lazy_html_obtainer import LazyHTMLObtainer
from selenium_html_obtainer import SeleniumHTMLObtainer
from file_downloader import FileDownloader
import config

from pathlib import Path
from aiogram.utils.chat_action import ChatActionSender
from aiogram import Router
from aiogram import types

message_router = Router()
message_parser = MessageParser()

lazy_html_obtainer = LazyHTMLObtainer()
selenium_html_obtainer = SeleniumHTMLObtainer()
html_parser = HTMLParser()
file_downloader = FileDownloader()

@message_router.message()
async def analyze_message(message: types.Message):
    if message.message_thread_id not in config.MONITORED_THREADS: # Monitoring only specified topics (threads)
        return
    list_of_urls = []
    article_urls = message_parser.parse(message.text)

    if not article_urls:
        return
    
    for url in article_urls:
        html = ""
        try:
            html = await lazy_html_obtainer.get_html(url)
        except:
            try:
                print(f"Processing {url} with Selenium.")
                html = await selenium_html_obtainer.get_html(url)
            except:
                with open(config.UNABLE_TO_DOWNLOAD_HISTORY, 'a') as file:
                    file.write(f"{url},")

        download_pdf_urls = html_parser.parse_for_download_links(url, html)
        list_of_urls.append(download_pdf_urls)

    for article_urls in list_of_urls:
        for url in article_urls:
            print(f"Trying to download from: {url}")
            status = file_downloader.download(url)
            if status:
                print("Download successful!")