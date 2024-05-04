import requests
import plotly.graph_objects as go
from plotly.offline import plot

# extracting cryptocurrency data from the API
def fetch_cryptocurrency_data(vs_currency='usd', per_page=10, page=1):
    url = 'https://api.coingecko.com/api/v3/coins/markets'
    params = {
        'vs_currency': vs_currency,
        'order': 'market_cap_desc',
        'per_page': per_page,
        'page': page
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print('Failed to fetch data from the API')
        return None

#plotting cryptocurrency market caps
def plot_cryptocurrency_market_caps(data, title):
    if data:
        coin_names = [coin['name'] for coin in data]
        market_caps = [coin['market_cap'] for coin in data]

        hover_text = [f'{name}: ${cap:,}' for name, cap in zip(coin_names, market_caps)]

        fig = go.Figure(data=[go.Bar(x=coin_names, y=market_caps, hovertext=hover_text, marker_color='steelblue')])
        fig.update_layout(title=title, xaxis_title='Cryptocurrency', yaxis_title='Market Cap (USD)', xaxis_tickangle=-45)
        plot(fig, filename=f'{title.lower().replace(" ", "_")}.html')

#cryptocurrency data for top 20 cryptocurrencies by market cap
top_20_crypto_data = fetch_cryptocurrency_data(per_page=20)
plot_cryptocurrency_market_caps(top_20_crypto_data, 'Top 20 Cryptocurrencies by Market Cap')

#cryptocurrency data for first 10 cryptocurrencies being used right now
current_10_crypto_data = fetch_cryptocurrency_data(per_page=10)
plot_cryptocurrency_market_caps(current_10_crypto_data, 'First 10 Cryptocurrencies Being Used Right Now')
