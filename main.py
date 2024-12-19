import logging

from scripts.strategy_engine import execute_strategy
from scripts.api_connector import initialize_api

logging.basicConfig(filename="logs/live_trading_log.txt", level=logging.INFO)

def main():
    logging.info("Starting DDGPT Trading System")
    api = initialize_api()
    execute_strategy(api)
