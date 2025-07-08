import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()  # Looks for .env file automatically

API_KEY = os.getenv('BINANCE_API_KEY')
API_SECRET = os.getenv('BINANCE_API_SECRET')
TESTNET = os.getenv('TESTNET', 'true').lower() == 'true'

class BasicBot:
    def __init__(self):
        self.client = Client(API_KEY, API_SECRET, testnet=TESTNET)

# ---------------------- TOP OF FILE ----------------------
# Add this RIGHT AFTER imports (line 1)
print("✅ Script initialization successful!")  # <-- NEW DEBUG LINE


import logging
from binance import Client
from binance.exceptions import BinanceAPIException
import argparse
from datetime import datetime

print("✅ DEBUG: Script started - Phase 1 (Import checks passed)")

class BasicBot:
    def __init__(self, api_key, api_secret, testnet=True):
        print(f"🔧 DEBUG: Initializing BasicBot (Testnet Mode: {testnet})")
        
        try:
            self.client = Client(api_key, api_secret, testnet=testnet)
            self.client.verbose = True  # Enable HTTP traffic logging
            print("🔌 DEBUG: Binance client initialized successfully")
        except Exception as e:
            print(f"❌ DEBUG: Client initialization failed: {str(e)}")
            raise

        self.setup_logging()
        self.logger = logging.getLogger('trading_bot')
        self.logger.info("Bot initialized")
        print("📜 DEBUG: Logging system ready")

    def setup_logging(self):
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler('trading_bot.log'),
                logging.StreamHandler()
            ]
        )

    def validate_symbol(self, symbol):
        print(f"🔎 DEBUG: Validating symbol: {symbol}")
        try:
            exchange_info = self.client.futures_exchange_info()
            valid_symbols = [s['symbol'] for s in exchange_info['symbols']]
            is_valid = symbol.upper() in valid_symbols
            print(f"   {'✅' if is_valid else '❌'} Symbol validation result: {is_valid}")
            return is_valid
        except BinanceAPIException as e:
            self.logger.error(f"Symbol validation error: {e}")
            print(f"❌ DEBUG: Symbol validation crashed: {str(e)}")
            return False

    def place_market_order(self, symbol, side, quantity):
        print(f"🚀 DEBUG: Attempting MARKET {side} {quantity} {symbol}")
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type='MARKET',
                quantity=quantity
            )
            print(f"🎉 DEBUG: Order executed successfully:\n{order}")
            return order
        except BinanceAPIException as e:
            self.logger.error(f"Market order failed: {e}")
            print(f"❌ DEBUG: Order failed with status code {e.status_code}: {e.message}")
            raise

    # ... [Include other methods like place_limit_order with similar debug prints]

def parse_args():
    print("🛠️ DEBUG: Parsing command line arguments")
    parser = argparse.ArgumentParser(description='Binance Futures Trading Bot')
    parser.add_argument('--symbol', required=True, help='Trading symbol (e.g., BTCUSDT)')
    parser.add_argument('--side', required=True, choices=['BUY', 'SELL'], help='Order side')
    parser.add_argument('--type', required=True, choices=['MARKET', 'LIMIT', 'STOP_LIMIT'], help='Order type')
    parser.add_argument('--quantity', required=True, type=float, help='Order quantity')
    parser.add_argument('--price', type=float, help='Limit price')
    parser.add_argument('--stop_price', type=float, help='Stop price')
    return parser.parse_args()
print("\n🔧 Debug: Reached main execution block")  # <-- NEW DEBUG LINE

if __name__ == '__main__':
    API_KEY = 'z9J6uqstHBBgoQ4JMTN7Zu8wMw2XToimqkwwVObe5xZpAwwu8CizAZOTiOr66jGy'  # ← MUST replace with your keys!
    API_SECRET = 'your_api_secret_here'
    
    bot = BasicBot(API_KEY, API_SECRET)
    args = parse_args()
    
    # Validations
    if not bot.validate_symbol(args.symbol):
        exit(1)
    if not bot.validate_quantity(args.quantity):
        exit(1)
        
    # Order execution
    try:
        print(f"\n🚀 Attempting {args.type} order...")
        if args.type == 'MARKET':
            order = bot.place_market_order(args.symbol, args.side, args.quantity)
        # Add other order types here
        
        print("\n💎 SUCCESS! Order Details:")
        print(f"Symbol: {order['symbol']}")
        print(f"Side: {order['side']}")
        print(f"Quantity: {order['origQty']}")
        print(f"Status: {order['status']}")
        
    except Exception as e:
        print(f"\n💥 FAILED: {str(e)}")
        print("Check trading_bot.log for details")
    
    # Test API keys - REPLACE THESE WITH YOUR TESTNET KEYS!
    API_KEY = 'itsanjeevAPIkey'
    API_SECRET = 'your_api_secret_here'
    
    print("🔐 DEBUG: Loading API credentials")
    bot = BasicBot(API_KEY, API_SECRET)
    
    args = parse_args()
    print(f"⚙️ DEBUG: Parsed arguments: {vars(args)}")
    
    # Validate inputs
    if not bot.validate_symbol(args.symbol):
        print(f"❌ ERROR: Invalid symbol {args.symbol}")
        exit(1)
        
    # Simplified version:
if args.quantity <= 0:
    print("❌ ERROR: Quantity must be positive")
    exit(1)

    try:
        print(f"\n🚦 DEBUG: Attempting {args.type} order...")
        if args.type == 'MARKET':
            order = bot.place_market_order(args.symbol, args.side, args.quantity)
        elif args.type == 'LIMIT':
            order = bot.place_limit_order(args.symbol, args.side, args.quantity, args.price)
        elif args.type == 'STOP_LIMIT':
            order = bot.place_stop_limit_order(args.symbol, args.side, args.quantity, args.price, args.stop_price)
        
        print("\n💎 ORDER EXECUTED SUCCESSFULLY!")
        print(f"   Symbol: {order['symbol']}")
        print(f"   Side: {order['side']}")
        print(f"   Type: {order['type']}")
        print(f"   Quantity: {order['origQty']}")
        print(f"   Status: {order['status']}")
        
    except Exception as e:
        print(f"\n💥 CRITICAL ERROR: {str(e)}")
        print("Check trading_bot.log for details")