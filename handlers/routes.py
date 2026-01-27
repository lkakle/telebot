from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()

@router.message(Command("start"))
async def start(message: Message):
    await message.answer("Команды:\n/all_users_ids\n/help")

@router.message(Command("help"))
async def start(message: Message):
    await message.answer("Команды:\n/all_users_ids\n/help")



