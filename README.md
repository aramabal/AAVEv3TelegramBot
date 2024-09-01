# AAVEv3TelegramBot
Telegram Bot with Web3 Integration
This project sets up a Telegram bot that interacts with Ethereum smart contracts using Web3. The bot periodically fetches data from specified contracts and sends updates to a Telegram chat.

Prerequisites
Before running the bot, ensure you have the following:

Python 3.7+: The bot is developed using Python 3.7 or higher.
Telegram Bot Token: You need a Telegram bot token to interact with the Telegram API.
Web3 Provider URL: You need an Ethereum node URL for Web3 to interact with the Ethereum network.
ABI Files: Ensure ABI files for the contracts are available in the project directory.
Setup Instructions
Clone the Repository

bash
Copy code
git clone <repository_url>
cd <repository_directory>
Install Dependencies

Create a virtual environment and install the required Python packages:

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
Create a .env File

Create a .env file in the root of the project directory and add the following environment variables:

plaintext
Copy code
TELEGRAM_TOKEN=your_telegram_bot_token
WEB3_PROVIDER_URL=your_web3_provider_url
Replace your_telegram_bot_token with your actual Telegram bot token and your_web3_provider_url with the URL of your Web3 provider (e.g., Infura or Alchemy).

Add ABI Files

Ensure that the ABI files for the smart contracts are named as follows and placed in the root directory of the project:

proxy_contract_abi.json for the borrow contract
supply_contract_abi.json for the supply contract
These ABI files should be JSON files that contain the ABI definitions for your smart contracts.

Run the Bot

To start the bot, simply run the main.py script:

bash
Copy code
python main.py
The bot will start, and you should see output indicating that it is connected to Web3 and ready to send messages.

Configuration
Contract Addresses: Update the following variables in main.py if the contract addresses change:

python
Copy code
CONTRACT_ADDRESS_BORROW = '0x0c84331e39d6658Cd6e6b9ba04736cC4c4734351'
CONTRACT_ADDRESS_SUPPLY = '0xe50fA9b3c56FfB159cB0FCA61F5c9D750e8128c8'
Replace these addresses with the addresses of your smart contracts.

Update ABI Files: Ensure that the ABI files match the contract ABI for the contracts you are interacting with. Any changes in the contract ABI may require updating the JSON files.

Troubleshooting
Web3 Connection Issues: Ensure that the WEB3_PROVIDER_URL is correct and that your Web3 provider is up and running.
Telegram Issues: Make sure your Telegram bot token is correct and that the bot has permissions to send messages.
Missing ABI Files: Check that the ABI files are in the correct format and located in the root directory of the project.
