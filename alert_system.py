# Alert System Module

import pandas as pd
import yfinance as yf

def filter_data_range(ticker, period, threshold):
    """Filters data within the given range and checks for alerts."""
    data = yf.download(ticker, period=period)
    filtered_data = data[data['Close'] < threshold]
    return filtered_data

def process_alert(filtered_data):
    """Processes the alert based on filtered data."""
    count = filtered_data['Close'].count()
    return count
