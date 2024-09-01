# Telegram Bot for Web3 Data Monitoring

This project is a Telegram bot that interacts with the Ethereum blockchain using Web3.py. It retrieves data from two smart contracts and sends periodic updates to a Telegram chat. The bot uses the Telegram API and Web3.py to accomplish its tasks.

## Features

- Connects to the Ethereum blockchain via Web3.
- Retrieves total supply data from two smart contracts.
- Converts the data from Wei to Ether.
- Calculates the utilization rate based on borrowed and supplied amounts.
- Sends periodic updates to a specified Telegram chat with formatted data.

## Prerequisites

Before running the bot, ensure you have the following:

1. **Python 3.8+**: This bot requires Python 3.8 or higher.
2. **Dependencies**: Install the required Python libraries.
3. **Environment Variables**: Set up your `.env` file with necessary credentials.

## Setup

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/your-username/your-repository.git
   cd your-repository
