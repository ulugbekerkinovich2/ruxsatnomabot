from aiogram.dispatcher.filters.state import State, StatesGroup



class Form(StatesGroup):
    chat_id = State()
    age = State()
    gender = State()