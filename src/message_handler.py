from tg_bot import bot
from message_parser import MessageParser
from link_parser import LinkParser
import config

from aiogram.utils.chat_action import ChatActionSender
from aiogram import Router
from aiogram import types

message_router = Router()
message_parser = MessageParser()
link_parser = LinkParser()

@message_router.message()
async def analyze_message(message: types.Message):
    article_url = message_parser.parse(message, message.text)
    download_pdf_url = link_parser.parse(article_url)
    await message.answer(text=ans)