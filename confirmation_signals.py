# Confirmation Signals Module

import pandas as pd
import numpy as np
import yfinance as yf

def calculate_signal_strength(ticker, period):
    """Calculates the signal strength based on market data."""
    data = yf.download(ticker, period=period)
    signal_strength = pd.DataFrame(data['Close'].rolling('2D').mean() > data['Close'].rolling('5D').mean())
    return signal_strength

def calculate_reverse_signal(ticker, period):
    """Calculates reverse signal strength based on market data."""
    data = yf.download(ticker, period=period)
    reverse_signal_strength = pd.DataFrame(data['Close'].rolling('2D').mean() < data['Close'].rolling('5D').mean())
    return reverse_signal_strength
