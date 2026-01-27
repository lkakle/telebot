from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

chat_id_name = []
chat_id_value = []

router = Router()

@router.message(Command("all_users_ids"))
async def all_users_ids(message: Message):
    if message.chat.id in chat_id_name:
        index = chat_id_name.index(message.chat.id)
        await message.answer("Id пользователей в базе: " + str(message.chat.full_name) + ":\n" + str(chat_id_value[index]))
    else:
        await message.answer( "Упс, похоже базы под именем: " + str(message.chat.full_name) + ": " + str(message.chat.id)+ "\nНету в списке, отправьте любое сообщение текстового формата, кроме команды, для регистрации.")

@router.message()
async def message_hundler(message: Message):
    if message.chat.id in chat_id_name:
        index = chat_id_name.index(message.chat.id)
        chat_id_value[index][message.from_user.id] = message.from_user.username
    else:
        chat_id_name.append(message.chat.id)
        value = dict()
        value[message.from_user.id] = message.from_user.username
        chat_id_value.append(value)