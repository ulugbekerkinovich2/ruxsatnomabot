from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton,WebAppInfo
from keyboards.default.menuKeyboard import contact_keyboard, dtm_keyboard
from loader import dp, bot
from data.config import CHANNEL_ID, CHANNEL_USERNAME, web_app_url
from aiogram.dispatcher import FSMContext
from states.userstate import Form
from utils.send_req import get_token, create_profile
from datetime import datetime

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message, state: FSMContext):
    token = await get_token()
    access = token.get('access')
    await state.update_data(token=access)
    user_id = message.from_user.id
    await state.update_data(user_id=user_id)
    name = message.from_user.first_name
    # print(message.from_user.first_name)
    sent_message = await message.answer(f"""
    👋 Assalomu alaykum, {name} botga xush kelibsiz.

    👇🏻 Botdan to'liq foydalanishni boshlash uchun 
    <b>«📲 Telefon raqamni yuborish»</b> tugmasini bosing.
    """, reply_markup=contact_keyboard)
    
    await state.update_data(last_message_id=sent_message.message_id)

@dp.message_handler(content_types=types.ContentTypes.CONTACT)
async def phone(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    chat_id = message.chat.id
    phone = message.contact.phone_number
    username = message.from_user.username
    lastname = message.from_user.last_name
    firstname = message.from_user.first_name
    token = await state.get_data()
    access = token.get('access')
    date_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(date_now)
    data = create_profile(access, chat_id, firstname, lastname, phone, username,date_now)
    print(data)
    await bot.delete_message(chat_id=user_id, message_id=message.message_id)

    data = await state.get_data()
    last_message_id = data.get('last_message_id')
    if last_message_id:
        await bot.delete_message(chat_id=user_id, message_id=last_message_id)

    user_status = await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=user_id)

    if user_status['status'] in ['member', 'administrator', 'creator']:
        sent_message = await bot.send_message(user_id, "Rahmat 😎, endi botdan to'liq foydalanishingiz mumkin.", reply_markup=types.ReplyKeyboardRemove())
        inline_kb = InlineKeyboardMarkup(row_width=1)
        subscribe_button = InlineKeyboardButton('📥Abituriyent ruxsatnomasini olish', url='https://my.uzbmb.uz/allow/bachelor-allow')
        
        # Create the second button
        exam_score_button = InlineKeyboardButton('📃Imtihon balini bilish', web_app=WebAppInfo(url=web_app_url))
        
        # Add both buttons to the inline keyboard
        inline_kb.add(subscribe_button, exam_score_button)

        sent_message = await bot.send_message(user_id, "Abituriyent ruxsatnomasini olish uchun quyidagi tugmani bosing:", reply_markup=inline_kb)
    else:
        inline_kb = InlineKeyboardMarkup(row_width=1)
        check_button = InlineKeyboardButton('✅ Obuna holatini tekshirish', callback_data='check_subscription')
        subscribe_button = InlineKeyboardButton('➕ Kanalga obuna bo\'lish', url=f'https://t.me/{CHANNEL_USERNAME}')
        inline_kb.add(subscribe_button, check_button)
        # Send the subscription message and store the message ID
        sent_message = await bot.send_message(user_id, "<b>Botdan foydalanishda davom etish uchun quyidagi kanallarimizga obuna bo'ling.</b>", reply_markup=inline_kb, parse_mode="HTML")
    
    await state.update_data(last_message_id=sent_message.message_id)



@dp.callback_query_handler(lambda c: c.data == 'check_subscription')
async def check_subscription(callback_query: types.CallbackQuery, state: FSMContext):
    user_id = callback_query.from_user.id
    user_status = await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=user_id)
    if user_status['status'] in ['member', 'administrator', 'creator']:
        data = await state.get_data()
        last_message_id = data.get('last_message_id')
        if last_message_id:
            await bot.delete_message(chat_id=user_id, message_id=last_message_id)
        # Send the DTM keyboard message and store the message ID
        sent_message = await bot.send_message(user_id, "Rahmat 😎, endi botdan to'liq foydalanishingiz mumkin.")
        inline_kb = InlineKeyboardMarkup(row_width=1)
        subscribe_button = InlineKeyboardButton('📥Abituriyent ruxsatnomasini olish', url='https://my.uzbmb.uz/allow/bachelor-allow')
        inline_kb.add(subscribe_button)

        await bot.send_message(user_id, "Abituriyent ruxsatnomasini olish uchun quyidagi tugmani bosing:", reply_markup=inline_kb)
    else:
        await bot.answer_callback_query(callback_query.id, text="Siz hali kanalga obuna bo'lmagansiz.", show_alert=True)
