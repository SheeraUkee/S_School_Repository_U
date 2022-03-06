from aiogram import executor
from loader import dp
from handlers.users.commands import start

start.register_chosen_inline_handler__command_start(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)