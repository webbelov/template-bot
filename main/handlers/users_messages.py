from aiogram import Router, F, Bot
from keyboards import inline
from aiogram.types import Message

router = Router()


@router.message(F.text.lower() == "да")
async def answer_yes(message: Message):
    await message.answer("Поехали!")


@router.message()
async def echo_handler(message: Message, bot: Bot) -> None:
    await message.answer(f"Я не понимаю. Нажмите кнопку /start для начала")
