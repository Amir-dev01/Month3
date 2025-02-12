from aiogram import Dispatcher
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State


# FSM - finite state machine
class Complaint(StatesGroup):
    name = State()
    phone_number = State()
    rate = State()
    extra_comments = State()


async def start_dialog(callback: CallbackQuery):
    await Complaint.name.set()
    await callback.message.answer("Как вас зовут")


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

    async with state.proxy() as data:
        data["rate"] = message.text
    await Complaint.next()
    await message.answer("Введите ваш отзыв")

async def process_extra_comments(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data["extra_comments"] = message.text
    await state.finish()
    await message.answer("Спасибо за отзыв.")


def register_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(start_dialog, lambda c: c.data == "review")
    dp.register_message_handler(process_name, state=Complaint.name)
    dp.register_message_handler(process_phone_number,state=Complaint.phone_number)
    dp.register_message_handler(process_rate, state=Complaint.rate)
    dp.register_message_handler(process_extra_comments, state=Complaint.extra_comments)