import ccxt
import time

# Create a Binance Futures exchange object
exchange = ccxt.binance()

# Load your API keys
exchange.apiKey = 'u1FIFY2Mdhpm06ggZgIOHRfKqvixAsybEfrKYMX9xlM24dGMtog77TLsYaDn8EKR'
exchange.secret = '2wcKsrevlLUX8Crfqp4E6NjvHy57pWqXDuTvKDLZaCmq3KCiOlQEXRJgADJ883f5'

# Set the symbol for the contract you want to trade (e.g. BTC/USDT)
symbol = 'BTC/USDT'

# Set the amount of contracts you want to trade
amount = 1

# Set the leverage for the trade
leverage = 5

# Set the initial stop loss and take profit prices (e.g. 5% below and 10% above entry price)
stop_loss = 0 #Dont change this!
take_profit =  #Set Take Profit Trigger

while True:
    # Get the current price of the contract
    price = exchange.fetch_ticker(symbol)['last']

    # Check if the stop loss and take profit have not been set yet
    if stop_loss == 0:
        # Set the stop loss and take profit prices based on the current price
        stop_loss = price * 0.95

        # Place a market order to buy
        order = exchange.create_order(symbol, 'market', 'buy', amount, {'leverage': leverage, 'stop_loss': stop_loss, 'take_profit': take_profit})
        print(f'Bought {amount} contracts at price {price} with stop loss {stop_loss} and take profit {take_profit}')
    # Check if the stop loss has been triggered
    elif price <= stop_loss:
        # Reset the stop loss and take profit prices
        stop_loss = 0
        take_profit = 0

        # Place a market order to sell
        order = exchange.create_order(symbol, 'market', 'sell', amount, {'leverage': leverage})
        print(f'Sold {amount} contracts at price {price} (stop loss triggered)')
    # Check if the take profit has been triggered
    elif price >= take_profit:
        # Reset the stop loss and take profit prices
        stop_loss = 0
        take_profit = 0

        # Place a market order to sell
        order = exchange.create_order(symbol, 'market', 'sell', amount, {'leverage': leverage})
        print(f'Sold {amount} contracts at price {price} (take profit triggered)')

    # Sleep for 1 hour
    time.sleep(60)
