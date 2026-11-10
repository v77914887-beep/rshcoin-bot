import os
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

# Получаем токен из переменной окружения Railway
TOKEN = os.getenv("BOT_TOKEN")
# Получаем ссылку на мини-приложение (вы ее настраивали ранее в Railway)
WEBAPP_URL = os.getenv("WEBAPP_URL")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Создаем клавиатуру с кнопкой открытия мини-приложения
    markup = InlineKeyboardMarkup()
    web_app = WebAppInfo(url=WEBAPP_URL)
    markup.add(InlineKeyboardButton("🛍 Открыть магазин и игру RSH Coin", web_app=web_app))
    
    bot.send_message(
        message.chat.id, 
        "👋 Привет! Добро пожаловать в официальный магазин и крипто-кликер RSH Coin.\n\nНажмите кнопку ниже, чтобы начать игру и зайти в магазин!",
        reply_markup=markup
    )

if __name__ == "__main__":
    print("Бот запущен...")
    bot.infinity_polling()


