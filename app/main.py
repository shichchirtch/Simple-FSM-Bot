import asyncio
from aiogram import Bot, Dispatcher
import game_handlers
import command_handlers
from bot_base import init_models
from aiogram.enums import ParseMode
from bot_states import no_redis
from config import settings


# Функция конфигурирования и запуска бота
async def main():
    await init_models()
    # Инициализируем бот и диспетчер
    bot = Bot(token=settings.BOT_TOKEN,
    parse_mode=ParseMode.HTML)

    # `default = DefaultBotProperties(...)


    dp = Dispatcher(storage=no_redis)
    # Регистрируем роутеры в диспетчере
    dp.include_router(command_handlers.command_router)
    dp.include_router(game_handlers.game_router)
    # Пропускаем накопившиеся апдейты и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

asyncio.run(main())