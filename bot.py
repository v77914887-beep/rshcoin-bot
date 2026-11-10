import asyncio
import os
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = os.getenv("BOT_TOKEN")
WEBAPP_URL = os.getenv("WEBAPP_URL")

if not BOT_TOKEN:
    raise ValueError("Не задан BOT_TOKEN в переменных окружения!")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🛍 Открыть магазин RSH Coin",
                    web_app=WebAppInfo(url=WEBAPP_URL or "https://example.com")
                )
            ]
        ]
    )
    
    await message.answer(
        "👋 Привет! Добро пожаловать в официальный магазин **RSH Coin**.\n\n"
        "Нажмите кнопку ниже, чтобы открыть каталог товаров и совершить покупку!",
        reply_markup=keyboard,
        parse_mode="Markdown"
    )

async def main():
    print("Бот магазина запущен и ждет сообщения...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())



