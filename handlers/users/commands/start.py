from aiogram import types, Dispatcher
# from TextMessage import *
from loader import dp, bot

@dp.message_handler(commands=["start"])
async def command_start(message: types.Message):
    bot.send_message(message.from_user.id, "Привет бот актевирован.")


def register_chosen_inline_handler__command_start(dp: Dispatcher):
    dp.register_chosen_inline_handler(dp)