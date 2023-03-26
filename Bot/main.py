import os
import re
from datetime import datetime

import toml
import logging
import asyncio

import frazes as RU

from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types.message import ContentType
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardButton, WebAppInfo, \
    InlineKeyboardMarkup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import Text, Command, RegexpCommandsFilter




logging.basicConfig(level=logging.INFO)

bot = Bot(token='6099531648:AAHb54wB_ToW_I4oI4bs6S0lMvcR7-23agM')
dp = Dispatcher(bot)


# main keyboard
b1_RU = KeyboardButton(RU.bt_1_kw_main)
b2_RU = KeyboardButton(RU.bt_2_kw_main)
b3_RU = KeyboardButton(RU.bt_3_kw_main)
keyboard = ReplyKeyboardMarkup(resize_keyboard=True)  # one_time_keyboard=True чтоб прятать клавиатуру

@dp.message_handler(Command("start"))
@dp.message_handler(Text("🏘 Домой"))
async def cmd_start(message: types.Message):
    kb = [
        types.KeyboardButton(text="Прислать геолокацию", request_location=True),
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)



    await message.answer(RU.RuStartPhrases, reply_markup=keyboard, parse_mode="Markdown")

# Start bot

# run long polling
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)