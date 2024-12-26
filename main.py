import logging
import os

from scripts.strategy_engine import execute_strategy
from scripts.api_connector import initialize_api

logging.basicConfig(filename="logs/live_trading_log.txt", level=logging.INFO)

def main():
    logging.info("Starting DDGPT Trading System")
    
    binance_api_key = os.getenv('BINANCE_API_KEY')
    binance_api_secret = os.getenv('BINANCE_API_SECRET')
    slack_webhook_url = os.getenv('SLACK_WEBHOOK_URL')
    
    api = initialize_api(binance_api_key, binance_api_secret)
    execute_strategy(api)

if __name__ == "__main__":
    main()
