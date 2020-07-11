from finnhub import client as Finnhub

client = Finnhub.Client(api_key="**************")

# Get real-time update on the number of COVID-19 (Coronavirus) cases in the US
# worked
print(client.covid())

# # Get general information of a company 
# worked
print(client.company_profile(symbol="NFLX"))

# # Get latest company's CEO compensation
# not worked
# print(client.ceo_compensation(symbol="NFLX"))

# # Get latest analyst recommendation trends
# worked 
print(client.recommendation(symbol="AAPL"))

# # Get latest price target consensus
#  worked 
print(client.price_target(symbol="NFLX"))

# # Get latest stock upgrade and downgrade
#  worked 
print(client.upgrade_downgrade(symbol="AAPL"))

# # Get company option chain
#  worked 
print(client.option_chain(symbol="NFLX"))

# # Get company peers
#  worked 
print(client.peers(symbol="NFLX"))

# # Get company quarterly earnings
#  worked 
print(client.earnings(symbol="NFLX"))

# # List supported stock exchanges
#  not worked 
# print(client.exchange())

# # List supported stocks
# worked
print(client.stock_symbol(exchange="US"))

# # Get quote data
# worked
print(client.quote(symbol="NFLX"))

# # Get candlestick data for stocks
# worked
print(client.stock_candle(symbol="NFLX", resolution="D", count=200))
print(client.stock_candle(symbol="NFLX", resolution="D", **{'from':'1575968404', 'to': '1575968424'}))

# # [PREMIUM] Get tick data
# worked
print(client.stock_tick(symbol="NFLX", resolution="D", **{'from':'1575968404', 'to': '1575968424'}))

# # List supported forex exchanges
# worked
print(client.forex_exchange())

# # List supported forex symbols
# worked
print(client.forex_symbol(exchange="oanda"))

# # Get candlestick data for forex symbols
# worked
print(client.forex_candle(symbol="OANDA:EUR_USD", resolution="D", count=200))

# # List supported crypto symbols by exchange\
# worked
print(client.crypto_symbol(exchange="binance"))

# # Get candlestick data for crypto symbols
# worked
print(client.crypto_candle(symbol="BINANCE:BTCUSDT", resolution="D", count=200))

# # Get pattern recognition on a symbol (support double top/bottom, triple top/bottom, head and shoulders, triangle, wedge, channel, flag, and candlestick patterns)
# worked
print(client.scan_pattern(symbol="NFLX", resolution="D"))

# # Get support and resistance levels for a symbol
# worked
print(client.scan_support_resistance(symbol="NFLX", resolution="D"))

# # Get aggregate signal of multiple technical indicators
# worked
print(client.scan_technical_indicator(symbol="NFLX", resolution="D"))

# # Get latest market news
# worked
print(client.news(category="general"))

# # List latest company news by symbol
# not worked
# print(client.company_news(symbol="NFLX"))

# # Get company's news sentiment and statistics
# worked
print(client.news_sentiment(symbol="NFLX"))

# # List countries where merger and acquisitions take place
# worked
print(client.merger_country())

# # List latest merger and acquisitions deal by country.
# worked
print(client.merger(country="United States"))

# # List codes of supported economic data
# worked
print(client.economic_code())

# # Get economic data
# worked
print(client.economic(code="MA-USA-G"))

# # Get recent and coming economic releases
# worked
print(client.calendar_economic())

# # Get recent and coming earnings release
# worked
print(client.calendar_earnings())

# # Get recent and coming IPO
# worked
print(client.calendar_ipo())

# # Get recent and coming ICO
# not worked
# print(client.calendar_ico())
