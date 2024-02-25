import logging
import sys
import os
from dotenv import load_dotenv
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.client import default


from handlers import users_commands, users_messages
from filters import users_filter
from callback import users_callback
from misc import bot_commands

from middlewares.throttling import ThrottlingMiddleware


load_dotenv()

TOKEN = os.getenv("API_KEY")
ADMIN_ID = os.getenv("ADMIN_ID")


async def main() -> None:
    dp = Dispatcher()
    bot = Bot(TOKEN, default=default.DefaultBotProperties(parse_mode='html'))
    await bot.send_message(ADMIN_ID, 'Бот запущен')
    dp.message.middleware(ThrottlingMiddleware())

    dp.include_routers(
        users_commands.router,
        users_messages.router,
        users_filter.router,
        users_callback.router,
    )
    await bot.set_my_commands(bot_commands.commands)
    await dp.start_polling(bot, skip_updates=True)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
