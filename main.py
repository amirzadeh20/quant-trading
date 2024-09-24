import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

# Define the stock symbol and the time period
symbol = 'AAPL'
start_date = '2020-01-01'
end_date = '2023-01-01'

# Fetch historical stock data
data = yf.download(symbol, start=start_date, end=end_date)

# Calculate short and long moving averages
short_window = 50  # Short moving average window
long_window = 200   # Long moving average window

data['Short_MA'] = data['Adj Close'].rolling(window=short_window, min_periods=1).mean()
data['Long_MA'] = data['Adj Close'].rolling(window=long_window, min_periods=1).mean()

# Generate signals
data['Signal'] = 0  # Default to no position
data['Signal'][short_window:] = np.where(data['Short_MA'][short_window:] > data['Long_MA'][short_window:], 1.0, 0.0)  # Buy signal
data['Position'] = data['Signal'].diff()  # Position change

# Plotting the results
plt.figure(figsize=(14, 7))
plt.plot(data['Adj Close'], label='Adjusted Close Price', alpha=0.5)
plt.plot(data['Short_MA'], label='50-Day Moving Average', alpha=0.75)
plt.plot(data['Long_MA'], label='200-Day Moving Average', alpha=0.75)

# Plot buy signals
plt.plot(data[data['Position'] == 1].index,
         data['Short_MA'][data['Position'] == 1],
         '^', markersize=10, color='g', lw=0, label='Buy Signal')

# Plot sell signals
plt.plot(data[data['Position'] == -1].index,
         data['Short_MA'][data['Position'] == -1],
         'v', markersize=10, color='r', lw=0, label='Sell Signal')

plt.title(f'{symbol} Moving Average Crossover Strategy')
plt.xlabel('Date')
plt.ylabel('Price in USD')
plt.legend()
plt.grid()
plt.show()
