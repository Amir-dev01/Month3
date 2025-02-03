import random
import asyncio
from aiogram import Bot, Dispatcher
from dotenv import dotenv_values


token = dotenv_values(".env")["BOT_TOKEN"]
bot = Bot(token=token)
dp = Dispatcher(bot)


unique_users = set()
@dp.message_handler(commands= ['start'])
async def start_handler(message):
    user = message.from_user
    unique_users.add(user.id)
    await message.answer(f"Привет, {user.first_name}, наш бот обслуживает уже {len(unique_users)} пользователей.")


@dp.message_handler(commands= ['myinfo'])
async def info_handler(message):
    user = message.from_user
    await message.answer(f"Ваше имя: {user.first_name} ")

    if user.last_name is not None:
        await message.answer(f"Ваша фамилия {user.last_name} ")

    await message.answer(f"ваш id: {user.id}")

    if user.username is not None:
        await message.answer (f"Ваш никнейм {user.username}")

names = ["Alex","John","Peter","Steve","Robert"]

@dp.message_handler(commands= ['random'])
async def info_handler(message):
    random_name = random.choice(names)
    await message.reply (f"Случайное имя {random_name}")


async def main():
    # запуск бота
    await dp.start_polling()

if __name__ == "__main__":
    asyncio.run(main())