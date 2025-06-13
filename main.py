import os
from dotenv import load_dotenv, find_dotenv
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Проверка наличия файла .env и загрузка токена
if not find_dotenv():
    print("Файл .env не найден! Создайте файл .env в корневой папке и добавьте строку BOT_TOKEN=ваш_токен.")
    exit()

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    print("Токен не найден в файле .env! Убедитесь, что в файле есть строка BOT_TOKEN=ваш_токен.")
    exit()

# Обработчик команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [['Старт']]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text(
        "Добро пожаловать в бота! Нажмите 'Старт', чтобы узнать больше о нем.",
        reply_markup=reply_markup
    )

# Обработчик текстовых сообщений
async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text == "Старт":
        await update.message.reply_text("Привет! Я ваш бот-помощник. Чем могу помочь?")
        context.user_data['started'] = True
    else:
        await update.message.reply_text("Пошел нахуй чушка ебаная хули ты сюда звонишь. Шляпа коровья")

def main():
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler))

    application.run_polling()

if __name__ == '__main__':
    main()




