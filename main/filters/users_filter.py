from aiogram import Router, F, Bot
from keyboards import inline
from aiogram.types import Message
from data import db

router = Router()

@router.message(F.text.lower() == "нет")
async def text_user(message: Message):
    await message.answer("Поиск...")





    

            
    







            





