from aiogram import Dispatcher
from aiogram.types import Message, CallbackQuery

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def flats_keyboard(name: str, data: dict):
    """Создаем клавиатуру с предложением."""
    # Создаем Клавиатуру
    markup = InlineKeyboardMarkup(row_width=1)

    markup.inline_keyboard = [
        [
            InlineKeyboardButton(
                text='Показать предложения',
                callback_data='show_offers',
                name=name,  # Передаю **kwargs
                data=data  # Передаю **kwargs
            )
        ],
        [
            InlineKeyboardButton(
                text='Заказать обратный звонок',
                callback_data='contact'
            )
        ]
    ]

    return markup


async def offers(message: Message, **kwargs):
    """Предлагаем на выбор."""
    data = {'Phone': 'Apple', 'Colour': 'Grey'}
    name = 'Some name'
    markup = await flats_keyboard(name, data)
    await message.answer(text='Подобрал для вас варианты, смотрим?', reply_markup=markup)


async def show_flats(call: CallbackQuery, **kwargs):
    data = kwargs  # Не могу отловить **kwargs
    await call.message.answer("The best")
    # Тут будет другая логика


def register_offers(dp: Dispatcher):
    dp.register_message_handler(offers, commands=["offers"], state="*")
    dp.register_callback_query_handler(show_flats, text='show_offers', state='*')
