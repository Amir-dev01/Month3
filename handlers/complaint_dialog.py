from aiogram import Dispatcher
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher.filters import Text

from bot_config import database


# FSM - finite state machine
class Complaint(StatesGroup):
    name = State()
    phone_number = State()
    rate = State()
    text = State()


async def start_dialog(callback: CallbackQuery):
    await Complaint.name.set()
    await callback.message.answer("Как вас зовут")


async def stop_dialog(message: Message, state: FSMContext):
    await state.finish()
    await message.answer("Спасибо за потраченное время")


async def process_name(message: Message, state: FSMContext):
    name = message.text
    async with state.proxy() as data:
        data["name"] = name
    await Complaint.next()
    await message.answer("Введите ваш номер телефона")


async def process_phone_number(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data["phone_number"] = message.text
    await Complaint.next()
    await message.answer("Поставьте нам оценку от 1 до 5?")


async def process_rate(message: Message, state: FSMContext):
    rate = message.text
    if not rate.isdigit():
        await message.answer('Введите число')
        return
    rate = int(rate)
    if rate < 1 or rate > 5:
        await message.answer('Неподходящая оценка!')
        return
    async with state.proxy() as data:
        data['rate'] = int(message.text)
    await Complaint.next()
    await message.answer('Можете оставить отзыв')


async def process_extra_comments(message: Message, state: FSMContext):

    async with state.proxy() as data:
        data["extra_comments"] = message.text

    extra_comments = data.get("extra_comments", "")


    database.add_complaint({
        "name": data["name"],
        "phone_number": data["phone_number"],
        "rate": data["rate"],
        "text": extra_comments
    })


    await state.finish()
    await message.answer("Спасибо за отзыв.")


def register_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(start_dialog, lambda c: c.data == "review")
    dp.register_message_handler(stop_dialog, Text(equals="stop"), state="*")
    dp.register_message_handler(process_name, state=Complaint.name)
    dp.register_message_handler(process_phone_number, state=Complaint.phone_number)
    dp.register_message_handler(process_rate, state=Complaint.rate)
    dp.register_message_handler(process_extra_comments, state=Complaint.text)
