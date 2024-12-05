import logging
import asyncio
from telegram.ext import ApplicationBuilder, ContextTypes
from bs4 import BeautifulSoup
import requests
from dotenv import load_dotenv
import os

## load environment variables 
load_dotenv()

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

Token = os.getenv('Token')
GROUP_ID = os.getenv('GROUP_ID')


def get_solana_price():
    url = "https://coinmarketcap.com/currencies/solana/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html')
    text = soup.find(id='section-coin-overview')
    price_element = text.find('span', class_='sc-65e7f566-0 WXGwg base-text')
    return price_element.text if price_element else 'Price not found'

async def send_price(context: ContextTypes.DEFAULT_TYPE):
    price = get_solana_price()
    message = f"The current price of Solana is {price}."
    await context.bot.send_message(chat_id=GROUP_ID, text=message)

async def start(update, context):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Bot is now running!")

if __name__ == '__main__':
    application = ApplicationBuilder().token(Token).build()
    
    application.job_queue.run_repeating(send_price, interval=20, first=10)  # Every hour
    
    application.run_polling()