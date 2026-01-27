from os import getenv
import asyncio
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from handlers import routes, weather, base

load_dotenv()


async def main():

    bot = Bot(token=getenv("BOT_TOKEN"))
    dp = Dispatcher()
    dp.include_routers(routes.router, weather.router, base.router)
    
    print("Start...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())