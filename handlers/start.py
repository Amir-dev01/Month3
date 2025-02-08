from aiogram import Dispatcher, types
from aiogram.types import (
    Message,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    CallbackQuery,
)

async def start_handler(message:types.Message):
    keyb = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardMarkup(text='Наш адрес',callback_data='address'),
            InlineKeyboardButton(text='Контакты',callback_data='contacts'),
        ],
        [
            InlineKeyboardButton(text='Сайт',url = 'https://dodopizza.kg/bishkek'),
            InlineKeyboardButton(text='Инстаграм',url = 'https://www.instagram.com/dodopizzakg/?hl=ru'),
        ],
        [
            InlineKeyboardButton(text='Оставить отзыв', callback_data = 'feedback'),
            InlineKeyboardButton(text='Наши вакансии', callback_data = 'vacancy'),
        ],
        [
            InlineKeyboardButton(text='Меню',callback_data = 'menu'),
            InlineKeyboardButton(text='О нас',callback_data = 'about')
        ]
    ])
    await message.answer(f'Здравствуйте {message.from_user.first_name}, это бот  Dodo Pizza',reply_markup=keyb)

async def address_handler(callback: CallbackQuery):
    await callback.message.answer('Юнусалиева 179/2')

async def contacts_handler(callback: CallbackQuery):
    await callback.message.answer('0551550550')

async def feedback_handler(callback: CallbackQuery):
    await callback.message.answer('Мы всегда рады вашим отзывам')

async  def vacancy_handler(callback: CallbackQuery):
    await callback.message.answer('Вакансии: Кассир, Пекарь, Уборщик')

async  def menu_handler(callback: CallbackQuery):
    await callback.message.answer('Пицца с пеперони, Пицца с сыром, Пицца с грибами')

async  def about(callback: CallbackQuery):
    await  callback.message.answer('Пицца на любой вкус только в Dodo Pizza')

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=["start"])
    dp.register_callback_query_handler(address_handler, lambda c: c.data == "address")
    dp.register_callback_query_handler(contacts_handler, lambda c: c.data == "contacts")
    dp.register_callback_query_handler(feedback_handler, lambda c: c.data == "feedback")
    dp.register_callback_query_handler(vacancy_handler, lambda c: c.data == "vacancy")
    dp.register_callback_query_handler(menu_handler, lambda c: c.data == "menu")
    dp.register_callback_query_handler(about, lambda c: c.data == "about")
