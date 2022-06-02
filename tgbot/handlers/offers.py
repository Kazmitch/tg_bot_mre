from aiogram import Dispatcher
from aiogram.types import Message

from tgbot.keyboards.inline import flats_keyboard


async def offers(message: Message, **kwargs):
    """Предлагаем квартиры на выбор."""
    data = {'Phone': 'Apple', 'Colour': 'Grey'}
    name = 'Some name'
    markup = await flats_keyboard(name, data)
    await message.answer(text='Подобрал для вас варианты, смотрим?', reply_markup=markup)


def register_offers(dp: Dispatcher):
    dp.register_message_handler(offers, commands=["offers"], state="*")
