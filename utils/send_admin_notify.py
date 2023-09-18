import os

from dotenv import load_dotenv


async def send_notify_start(bot):
    load_dotenv()
    admins = os.getenv('ADMINS').split(',')
    for admin in admins:
        await bot.send_message(admin, 'Бот запущен!')


async def send_notify_finish(bot):
    load_dotenv()
    admins = os.getenv('ADMINS').split(',')
    for admin in admins:
        await bot.send_message(admin, 'Бот остановлен!')
