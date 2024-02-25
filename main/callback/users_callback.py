from aiogram import Router, F, Bot
from aiogram import types
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.filters.callback_data import CallbackData
from data import db

router = Router()

class AddProductCallbackFactory(CallbackData, prefix="product"):
    action: str
    value:  str    


@router.callback_query(AddProductCallbackFactory.filter(F.action == "startBtn"))
async def send_random_value(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer('Начали!')
    await callback.answer()


@router.callback_query(AddProductCallbackFactory.filter(F.action == "stopBtn"))
async def send_random_value(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer('Закончили!')
    await callback.answer()

















