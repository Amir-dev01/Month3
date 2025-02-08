from aiogram import Dispatcher, types
from bot_config import dp


unique_users = set()


# @dp.message_handler(commands= ['myinfo'])
async def info_handler(message):
    user = message.from_user
    await message.answer(f"Ваше имя: {user.first_name} ")

    if user.last_name is not None:
        await message.answer(f"Ваша фамилия {user.last_name} ")

    await message.answer(f"ваш id: {user.id}")

    if user.username is not None:
        await message.answer (f"Ваш никнейм {user.username}")

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(info_handler, commands=['myinfo'])