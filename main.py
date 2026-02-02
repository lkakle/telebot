from dotenv import load_dotenv
import os
import asyncio
from aiogram import Bot, Dispatcher
from handlers import routes, weather, ai_chat, base

load_dotenv()


async def main():

    bot = Bot(token=os.getenv("TOKEN"))
    dp = Dispatcher()
    dp.include_routers(routes.router, weather.router, ai_chat.router, base.router)
    
    print("Start...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main()) 