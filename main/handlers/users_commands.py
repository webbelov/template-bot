from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

#Импорт клавиатур
from keyboards import inline, reply

router = Router()


@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer("<b>Готов к работе!</b>")


@router.message(Command(commands=["help"]))
async def cmd_start(message: Message):
    await message.answer("Разработка ботов webbelov.ru", reply_markup=reply.default_keyboard())


@router.message(Command(commands=["testdef"]))
async def cmd_start(message: Message):
    await message.answer("Тестируем?",  reply_markup=inline.start_walk_inline())


