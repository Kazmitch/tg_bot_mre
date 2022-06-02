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
