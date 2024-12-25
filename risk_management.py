# Risk Management Module

import yfinance as yf

def calculate_risk(ticker, period, threshold):
    """Calculates the risk based on the given threshold."""
    data = yf.download(ticker, period=period)
    rolling_data = data['Close'].rolling(window=5).mean()
    if rolling_data.iloc[-1] > threshold:
        return "Modify Gain"
    elif rolling_data.iloc[-1] < threshold * 0.5:
        return "Lead Gain"

def calculate_uncertainty(threshold, gain_threshold):
    """Calculates uncertainty based on thresholds."""
    if threshold * 0.1 > gain_threshold:
        return "Critical Uncertainty"
    else:
        return "Compensated Uncertainty"
