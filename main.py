import logging
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import random

# Включаем логирование
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

# Функция для команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    reply_keyboard = [['/help', '/random']]
    await update.message.reply_text(
        'Привет! Я бот для таблицы умножения. Введите /help для получения инструкций.',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    )

# Функция для команды /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        'Команды:\n'
        '/table <число> - Получить таблицу умножения для указанного числа.\n'
        '/range <число1> <число2> - Получить таблицы умножения для диапазона чисел.\n'
        '/random - Получить таблицу умножения для случайного числа.'
    )

# Функция для команды /table
async def table(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        number = int(context.args[0])
        multiplication_table = '\n'.join([f"{number} * {i} = {number * i}" for i in range(1, 11)])
        await update.message.reply_text(multiplication_table)
    except (IndexError, ValueError):
        await update.message.reply_text('Пожалуйста, введите правильное число после команды /table.')

# Функция для команды /range
async def range_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        number1 = int(context.args[0])
        number2 = int(context.args[1])
        tables = []
        for number in range(number1, number2 + 1):
            table = '\n'.join([f"{number} * {i} = {number * i}" for i in range(1, 11)])
            tables.append(f"Таблица умножения для {number}:\n{table}")
        await update.message.reply_text('\n\n'.join(tables))
    except (IndexError, ValueError):
        await update.message.reply_text('Пожалуйста, введите правильные числа после команды /range.')

# Функция для команды /random
async def random_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    number = random.randint(1, 10)
    multiplication_table = '\n'.join([f"{number} * {i} = {number * i}" for i in range(1, 11)])
    await update.message.reply_text(f"Случайное число: {number}\n{multiplication_table}")

def main() -> None:
    # Вставьте сюда ваш токен
    token = '5465871738:AAEh9m3qkJAnQvz_j2lSxPTuPiGigkAVaSU'

    # Создаем Application и передаем ему токен вашего бота
    application = ApplicationBuilder().token(token).build()
    
    # Обработчики команд
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("table", table))
    application.add_handler(CommandHandler("range", range_command))
    application.add_handler(CommandHandler("random", random_command))

    # Запускаем бота
    application.run_polling()

if __name__ == '__main__':
    main()
