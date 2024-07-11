from loader import dp
from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from aiogram.dispatcher.filters import Text
from data.config import web_app_url
from aiogram.dispatcher import FSMContext
from keyboards.default.menuKeyboard import contact_keyboard,dtm_keyboard

@dp.message_handler(Text(equals='📥Ruxsatnomani olish'), state="*")
async def send_about_info(message: types.Message, state: FSMContext):
    # Create an inline keyboard button with a URL
    inline_kb = InlineKeyboardMarkup(row_width=1)
    subscribe_button = InlineKeyboardButton('📥Abituriyent ruxsatnomasini olish', url='https://my.uzbmb.uz/allow/bachelor-allow')
    inline_kb.add(subscribe_button)
    

    await message.reply("Abituriyent ruxsatnomasini olish uchun quyidagi tugmani bosing:", reply_markup=inline_kb)