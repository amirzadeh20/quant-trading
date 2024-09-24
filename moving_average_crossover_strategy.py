import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt

# Fetch historical stock data
symbol = 'AAPL'
data = yf.download(symbol, start='2020-01-01', end='2023-01-01')

# Calculate moving averages
short_window = 50
long_window = 200
data['Short_MA'] = data['Adj Close'].rolling(window=short_window).mean()
data['Long_MA'] = data['Adj Close'].rolling(window=long_window).mean()

# Generate signals
data['Signal'] = np.where(data['Short_MA'] > data['Long_MA'], 1.0, 0.0)
data['Position'] = data['Signal'].diff()

# Plotting the results
plt.figure(figsize=(14, 7))
plt.plot(data['Adj Close'], label='Adjusted Close Price', alpha=0.5)
plt.plot(data['Short_MA'], label='50-Day MA', alpha=0.75)
plt.plot(data['Long_MA'], label='200-Day MA', alpha=0.75)
plt.plot(data[data['Position'] == 1].index, 
         data['Short_MA'][data['Position'] == 1], 
         '^', markersize=10, color='g', lw=0, label='Buy Signal')
plt.plot(data[data['Position'] == -1].index, 
         data['Short_MA'][data['Position'] == -1], 
         'v', markersize=10, color='r', lw=0, label='Sell Signal')
plt.title(f'{symbol} Moving Average Crossover Strategy')
plt.xlabel('Date')
plt.ylabel('Price in USD')
plt.legend()
plt.grid()
plt.show()
