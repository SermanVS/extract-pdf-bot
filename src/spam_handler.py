from tg_bot import bot, InputStartsWithFilter

from aiogram import Router
from aiogram.types import Message
from aiogram.utils.chat_action import ChatActionSender

spam_router = Router()

@spam_router.message(InputStartsWithFilter("/"))
async def info_handler(message: Message):
    async with ChatActionSender.typing(bot=bot, chat_id=message.chat.id):
        text = "You are trying to use a command that doesn't exist. Please, check your prompt."
        await message.answer(text=text)
        
        