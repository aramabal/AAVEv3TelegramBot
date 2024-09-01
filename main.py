import os
import json
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackContext
from dotenv import load_dotenv
from web3 import Web3

# Load variables from .env file
load_dotenv()

# Configuration
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
WEB3_PROVIDER_URL = os.getenv('WEB3_PROVIDER_URL')

# Check for the presence of variables
if not TELEGRAM_TOKEN:
    print("Error: TELEGRAM_TOKEN is not set. Check the .env file.")
    exit(1)

if not WEB3_PROVIDER_URL:
    print("Error: WEB3_PROVIDER_URL is not set. Check the .env file.")
    exit(1)

# Contract addresses
CONTRACT_ADDRESS_BORROW = '0x0c84331e39d6658Cd6e6b9ba04736cC4c4734351'  # Borrow contract address
CONTRACT_ADDRESS_SUPPLY = '0xe50fA9b3c56FfB159cB0FCA61F5c9D750e8128c8'  # Supply contract address

# Load ABI from file
def load_abi(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except Exception as e:
        print(f"Error loading ABI from {file_path}: {e}")
        return None

# Initialize Web3
web3 = Web3(Web3.HTTPProvider(WEB3_PROVIDER_URL))

# Global variable to store chat_id
global_chat_id = None

def check_web3_connection():
    if web3.is_connected():
        print("Web3 is connected.")
    else:
        print("Error connecting to Web3.")

def get_total_supply(contract_address: str, abi_file: str) -> int:
    try:
        # Load ABI
        contract_abi = load_abi(abi_file)
        if contract_abi is None:
            return 0

        contract = web3.eth.contract(
            address=Web3.to_checksum_address(contract_address),
            abi=contract_abi
        )

        # Call totalSupply method
        total_supply = contract.functions.totalSupply().call()
        print(f"Retrieved totalSupply value for {contract_address}: {total_supply}")  # Debug message
        return total_supply
    except Exception as e:
        print(f"Error getting data: {str(e)}")
        return 0

def convert_to_ether(wei_value: int) -> float:
    # Convert wei to ether
    return web3.from_wei(wei_value, 'ether')

def calculate_utilization_rate(borrowed: float, supplied: float) -> float:
    # Check for division by zero
    if supplied == 0:
        return 0.0
    return (borrowed / supplied) * 100

async def start(update: Update, context: CallbackContext) -> None:
    global global_chat_id
    global_chat_id = update.message.chat_id
    await update.message.reply_text(f'Your chat_id: {global_chat_id}')

    # Check Web3 connection
    check_web3_connection()

    # Set up periodic task
    context.application.job_queue.run_repeating(
        check_data, interval=180, first=10  # Request every 3 minutes (180 seconds)
    )

async def check_data(context: CallbackContext) -> None:
    if global_chat_id is None:
        print("Error: chat_id is not set.")
        return

    try:
        print("Starting data check...")  # Debug message

        # Get totalSupply for borrow contract
        total_supply_borrow = get_total_supply(CONTRACT_ADDRESS_BORROW, 'borrow_contract_abi.json')
        total_supply_in_ether_borrow = convert_to_ether(total_supply_borrow) if total_supply_borrow else 0

        # Get totalSupply for supply contract
        total_supply_supply = get_total_supply(CONTRACT_ADDRESS_SUPPLY, 'supply_contract_abi.json')
        total_supply_in_ether_supply = convert_to_ether(total_supply_supply) if total_supply_supply else 0

        # Calculate utilization rate
        utilization_rate = calculate_utilization_rate(total_supply_in_ether_borrow, total_supply_in_ether_supply)

        # Format message with bold numbers and new lines
        message = (
            f"Total borrowed from 100k:\n"
            f"<b>{total_supply_in_ether_borrow:.4f} ETH</b>\n\n"
            f"Total supply from 140k:\n"
            f"<b>{total_supply_in_ether_supply:.4f} ETH</b>\n\n"
            f"Utilization Rate:\n"
            f"<b>{utilization_rate:.2f}%</b>"
        )

        await context.bot.send_message(chat_id=global_chat_id, text=message, parse_mode='HTML')
        
    except Exception as e:
        await context.bot.send_message(chat_id=global_chat_id, text=f"Error: {str(e)}")

def main() -> None:
    application = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.run_polling()

if __name__ == '__main__':
    main()
