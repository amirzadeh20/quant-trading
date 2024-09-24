# Quant Trading

## Explanation of the Code
- **Data Retrieval**: The code uses the yfinance library to fetch historical stock price data for Apple Inc. (AAPL) from January 1, 2020, to January 1, 2023.
- **Moving Averages Calculation**: It calculates two moving averages:
- A short moving average over a period of 50 days.
- A long moving average over a period of 200 days.
- **Signal Generation**: The code generates buy signals when the short moving average crosses above the long moving average and sell signals when it crosses below.
- **Visualization**: Finally, it visualizes the adjusted close price along with the moving averages and marks buy and sell signals on the plot.
This example provides a foundation for more complex strategies and can be expanded with additional features such as risk management, portfolio optimization, or integration with trading platforms for live execution.
