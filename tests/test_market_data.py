from src.market_data import MarketData

eurusd = CurrencyPair("EUR", "USD")

market = MarketData(
    pair=eurusd,
    spot=1.1735,
    domestic_rate=0.042,
    foreign_rate=0.021,
)

print(market)
