# Trade Execution Module

import smtplib
import yfinance as yf

def execute_trade(ticker, action):
    """Executes a trade based on the specified action."""
    if action not in ["buy", "sell"]:
        raise ValueError("Action must be 'buy' or 'sell'")
    message = f"{action.upper()} trade executed for {ticker}"
    print(message)  # Replace with email or logging

def execute_trade_with_amount(ticker, action, amount):
    """Executes a trade with a specified amount."""
    if action not in ["buy", "sell"]:
        raise ValueError("Action must be 'buy' or 'sell'")
    message = f"{action.upper()} trade executed for {amount} shares of {ticker}"
    print(message)  # Replace with email or logging
