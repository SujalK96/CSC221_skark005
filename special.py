import yfinance as yf
import matplotlib.pyplot as plt

# Fetching stock data for the given tickers and certain date range
def fetch_stock_data(tickers_list, start_date, end_date):
    return yf.download(tickers_list, start=start_date, end=end_date)['Adj Close']
# Here we plot and save the close price of stocks and we also use legends
def plot_stock_data(data, tickers_list):
    plt.figure(figsize=(10, 7))
    for ticker in tickers_list:
        data[ticker].plot(label=ticker)
    plt.title("Adjusted Close Prices of Stocks")
    plt.ylabel('Price')
    plt.xlabel('Year')
    plt.grid(which="major", color='k', linestyle='-.', linewidth=0.5)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    start_date = '1990-01-01'
    end_date = '2021-07-12'
    tickers_list = ['AAPL', 'IBM', 'MSFT', 'AMZN']
    data = fetch_stock_data(tickers_list, start_date, end_date)
    plot_stock_data(data, tickers_list)
