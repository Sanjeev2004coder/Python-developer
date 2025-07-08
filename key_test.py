from binance import Client

NEW_API_KEY = 'MYAPIKEY2004'  # Full 64-char key
NEW_API_SECRET = 'paste_new_secret_here'

try:
    print("🔐 Testing new keys...")
    client = Client(NEW_API_KEY, NEW_API_SECRET, testnet=True)
    
    # Basic connectivity test
    print("⏰ Server time:", client.get_server_time())
    
    # Futures balance check
    usdt_balance = next(
        (x for x in client.futures_account_balance() 
        if x['asset'] == 'USDT'), 
        None
    )
    print(f"💰 Testnet USDT Balance: {usdt_balance['balance'] if usdt_balance else '0'}")
    
except Exception as e:
    print(f"❌ Still failing: {str(e)}")
    if "code=-2015" in str(e):
        print("→ Confirm you're using TESTNET keys (not mainnet)")