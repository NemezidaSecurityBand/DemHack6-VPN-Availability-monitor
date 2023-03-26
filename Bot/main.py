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

config = toml.load(open("secrets.toml", 'r'))

bot = Bot(token=config['key'])
dp = Dispatcher(bot)

# main keyboard
b1_RU = KeyboardButton(RU.bt_1_kw_main)
b2_RU = KeyboardButton(RU.bt_2_kw_main)
b3_RU = KeyboardButton(RU.bt_3_kw_main)
keyboard = ReplyKeyboardMarkup(resize_keyboard=True)  # one_time_keyboard=True чтоб прятать клавиатуру


@dp.message_handler(Command("start"))
@dp.message_handler(Text(RU.bt_3_kw_main))
async def cmd_start(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text="Прислать геолокацию", request_location=True),
            types.KeyboardButton(text=RU.bt_4_kw_main)
        ]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)

    await message.answer(RU.RuStartPhrases, reply_markup=keyboard, parse_mode="Markdown")


@dp.message_handler(Text(RU.bt_4_kw_main))
@dp.message_handler(Command("check_connection"))
async def connection_check(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text=RU.bt_3_kw_main)
        ]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)

    await message.answer(RU.RuCheckConnection.replace('.', '\.'), reply_markup=keyboard, parse_mode="MarkdownV2")

# Start bot

# run long polling
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)