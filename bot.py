import asyncio
import logging
import os

from aiogram import Bot, Dispatcher
from aiogram.fsm.strategy import FSMStrategy
from aiogram.fsm.storage.memory import MemoryStorage
from dotenv import load_dotenv

from handlers import handler_start, handler_main_menu, handler_echo

# gs
from handlers.gs import handler_gs, handler_gs_mobile, handler_gs_computer, handler_gs_wash, handler_gs_av

from settings.bot_menu import set_main_menu
# from bot_db.bot_database import db_start

logger = logging.getLogger(__name__)
logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
)

load_dotenv()
bot: Bot = Bot(token=os.getenv('BOT_TOKEN'), parse_mode='html')
dp: Dispatcher = Dispatcher(storage=MemoryStorage(), fsm_strategy=FSMStrategy.USER_IN_CHAT)


# Запуск бота
async def main():

    logger.info("Starting bot")

    dp.include_routers(
        handler_start.router,
        handler_main_menu.router,
        # gs
        handler_gs.router,
        handler_gs_mobile.router,
        handler_gs_computer.router,
        handler_gs_wash.router,
        handler_gs_av.router,

        handler_echo.router,
    )

    # Пропускаем накопившиеся апдейты и запускаем polling
    # start
    try:
        await bot.delete_webhook(drop_pending_updates=True)
        # await send_notify(bot)
        dp.startup.register(set_main_menu)
        # await db_start()
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Bot stopped!")
