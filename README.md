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
   git clone https://github.com/aramabal/AAVEv3TelegramBot.git
   cd AAVEv3TelegramBot

2. **Create a `.env` File**

   Create a `.env` file in the root directory of your project and add the following lines, replacing the placeholders with your actual values:

   ```env
   TELEGRAM_TOKEN=your_telegram_bot_token
   WEB3_PROVIDER_URL=https://your.ethereum.node.url

## How to Obtain `WEB3_PROVIDER_URL`

To interact with the Ethereum blockchain, you need a Web3 provider URL. This URL connects your application to an Ethereum node, which allows you to query and send transactions to the blockchain. Here’s how you can obtain a `WEB3_PROVIDER_URL`:

1. **Using a Public Ethereum Node Provider**:
   - **Infura**:
     1. Go to [Infura's website](https://infura.io/).
     2. Sign up for a free account.
     3. Create a new project in the Infura dashboard.
     4. Choose "Ethereum" as the network and select the desired network (Mainnet, Ropsten, Rinkeby, etc.).
     5. Copy the Project ID and Project Secret.
     6. Construct your Web3 provider URL in the format:
        ```
        https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID
        ```
        Replace `mainnet` with the network of your choice and `YOUR_INFURA_PROJECT_ID` with your actual Infura Project ID.

   - **Alchemy**:
     1. Visit [Alchemy's website](https://www.alchemy.com/).
     2. Sign up for an account.
     3. Create a new app in the Alchemy dashboard.
     4. Choose Ethereum and select the desired network.
     5. Copy the HTTP URL from the app settings.
     6. The Web3 provider URL will be in the format:
        ```
        https://eth-mainnet.alchemyapi.io/v2/YOUR_ALCHEMY_API_KEY
        ```
        Replace `YOUR_ALCHEMY_API_KEY` with your actual Alchemy API key.

2. **Other Providers**:
   - There are several other providers such as [QuickNode](https://quiknode.io/), [Chainstack](https://chainstack.com/), and [Blockchair](https://blockchair.com/). The process for obtaining the URL is similar: sign up, create a project or node, and use the provided URL.

