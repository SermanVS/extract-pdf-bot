from aiogram import Router
from aiogram.types import Message
from tg_bot import bot, InputMatchesFilter, get_language
from pathlib import Path
from aiogram.utils.chat_action import ChatActionSender

command_router = Router()

@command_router.message(InputMatchesFilter("/info"))
async def info_handler(message: Message):
    info_filename = Path('predefined_texts') / 'info_response.md'
    async with ChatActionSender.typing(bot=bot, chat_id=message.chat.id):
        text = ""
        with open(info_filename, encoding="utf8") as f:
            text = f.read()
        await message.answer(text=text, parse_mode="markdown", disable_web_page_preview=True)

@command_router.message(InputMatchesFilter("/start"))
async def start_handler(message: Message):
    start_filename = Path('predefined_texts') / 'start_response.md'
    async with ChatActionSender.typing(bot=bot, chat_id=message.chat.id):
        text = ""
        with open(start_filename, encoding="utf8") as f:
            text = f.read()
        await message.answer(text=text, parse_mode="markdown", disable_web_page_preview=True)
        