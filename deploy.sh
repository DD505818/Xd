#!/bin/bash

# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Install jq
sudo apt-get update
sudo apt-get install -y jq

# Configure environment variables from api_keys.json
API_KEYS=$(cat api_keys.json | jq -r '.binance.api_key, .binance.api_secret, .slack.webhook_url')

export BINANCE_API_KEY=$(echo $API_KEYS | awk 'NR==1')
export BINANCE_API_SECRET=$(echo $API_KEYS | awk 'NR==2')
export SLACK_WEBHOOK_URL=$(echo $API_KEYS | awk 'NR==3')

# Deployment steps for alert system
echo "Deploying alert system..."
python alert_system.py

# Deployment steps for confirmation signals
echo "Deploying confirmation signals..."
python confirmation_signals.py

# Deployment steps for risk management
echo "Deploying risk management..."
python risk_management.py

# Deployment steps for trade execution
echo "Deploying trade execution..."
python trade_execution.py

echo "Deployment completed successfully."
