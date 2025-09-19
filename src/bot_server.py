from command_handler import command_router
from spam_handler import spam_router
from message_handler import message_router
from tg_bot import bot

from aiogram import Dispatcher
import asyncio

dp = Dispatcher()
dp.include_router(command_router)
dp.include_router(spam_router)
dp.include_router(message_router)

async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    main_loop = asyncio.new_event_loop()
    main_loop.create_task(main())
    main_loop.run_forever()
