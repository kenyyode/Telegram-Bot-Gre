# Solana Price Telegram Bot
This project is a Telegram bot that scrapes the current price of Solana (SOL) from CoinMarketCap and sends hourly updates to a designated Telegram group. Built using Python, it leverages the python-telegram-bot library for bot functionalities and Beautiful Soup for web scraping.

## Features
Real-time Price Updates: The bot fetches the latest price of Solana from CoinMarketCap.
Automated Messaging: Sends hourly updates to a specified Telegram group.
Error Handling: Ensures reliable price fetching and graceful fallback if data is unavailable.

## Tools and Technologies
Python
Telegram Bot API (python-telegram-bot)
BeautifulSoup (for web scraping)
Requests
dotenv (for environment variable management)