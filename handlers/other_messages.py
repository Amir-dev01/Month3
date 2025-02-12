from aiogram import Dispatcher,types

async def echo_handler(message):
    text = message.text
    await message.reply("Я вас не понимаю")


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(echo_handler())

