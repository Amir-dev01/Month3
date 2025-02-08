import random
from aiogram import Dispatcher, types
from bot_config import dp


names = ["Alex","John","Peter","Steve","Robert"]
# @dp.message_handler(commands= ['random'])
async def Random_handler(message):
    random_name = random.choice(names)
    await message.reply (f"Случайное имя {random_name}")

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(Random_handler, commands=['random'])