from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData

#Инлайн кнопки
class AddProductCallbackFactory(CallbackData, prefix="product"):
    action: str
    value:  str


def start_walk_inline() -> ReplyKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(text=f"Старт", callback_data=AddProductCallbackFactory(action="startBtn", value=f"test"))
    builder.button(text=f"Стоп", callback_data=AddProductCallbackFactory(action="stopBtn", value=f"test"))
    builder.adjust(1)
    return builder.as_markup()
