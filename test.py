import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
) ## this ensures that my bot logs important events which is import for debugging

Token = "7924804008:AAEbIaVWSJ7g64FIHZW_53ocj-d5jtqwoP4"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Hello, please talk to me!")

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Hello, welcome to a new day")

if __name__ == '__main__':
    application = ApplicationBuilder().token(Token).build()
    
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    hello_handler = CommandHandler('hello', hello)
    application.add_handler(hello_handler)
    
    application.run_polling() 