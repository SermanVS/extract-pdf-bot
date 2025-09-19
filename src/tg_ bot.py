import config
from aiogram.filters import Filter
from aiogram.types import Message
from aiogram import Bot

class InputMatchesFilter(Filter):
    def __init__(self, my_text: str) -> None:
        self.my_text = my_text

    async def __call__(self, message: Message) -> bool:
        return message.text == self.my_text

class InputStartsWithFilter(Filter):
    def __init__(self, my_text: str) -> None:
        self.my_text = my_text

    async def __call__(self, message: Message) -> bool:
        return message.text.startswith(self.my_text)

bot = Bot(token=config.API_KEY_TG)
