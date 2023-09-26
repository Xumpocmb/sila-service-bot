import asyncio
import logging
import os

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.strategy import FSMStrategy
from dotenv import load_dotenv

from handlers import handler_start, handler_docs, handler_main_menu, handler_echo, handler_prevention, \
    handler_gs, handler_installation, handler_insurance, handler_it_service
from handlers.admin_panel import handler_admin_main
from settings.bot_menu import set_main_menu

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
        handler_admin_main.router,
        handler_docs.router,
        handler_gs.router,
        handler_prevention.router,
        handler_installation.router,
        handler_insurance.router,
        handler_it_service.router,

        handler_echo.router,
    )

    # Пропускаем накопившиеся апдейты и запускаем polling
    # start
    try:
        await bot.delete_webhook(drop_pending_updates=True)
        # await send_notify_start(bot)
        dp.startup.register(set_main_menu)
        # await db_start()
        await dp.start_polling(bot)
    finally:
        # await send_notify_finish(bot)
        await bot.session.close()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Bot stopped!")
