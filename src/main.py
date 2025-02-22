from binance.client import Client
from binance.enums import SIDE_BUY, ORDER_TYPE_MARKET
import time

# Replace these with your Binance API keys
API_KEY = 'your_api_key_here'
API_SECRET = 'your_api_secret_here'

# Initialize the Binance client
client = Client(API_KEY, API_SECRET)

def get_latest_price(symbol):
    """Fetch the latest price for a given trading pair."""
    ticker = client.get_symbol_ticker(symbol=symbol)
    return float(ticker['price'])

def place_market_order(symbol, quantity, side):
    """Place a market order on Binance."""
    try:
        order = client.create_order(
            symbol=symbol,
            side=side,
            type=ORDER_TYPE_MARKET,
            quantity=quantity
        )
        print("Order placed successfully:")
        print(order)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    symbol = "BTCUSDT"  # Trading pair (Bitcoin to USDT)
    quantity = 0.001    # Amount of BTC to buy (adjust as needed)

    # Fetch the latest price
    price = get_latest_price(symbol)
    print(f"Latest price of {symbol}: {price} USDT")

    # Place a market order to buy BTC
    print(f"Placing a market order to buy {quantity} {symbol}...")
    place_market_order(symbol, quantity, SIDE_BUY)