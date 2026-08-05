from project_quant.market_data import MarketData
from project_quant.currency import CurrencyPair


def test_market_data_creation():
    eurusd = CurrencyPair("EUR", "USD")

    market = MarketData(
        pair=eurusd,
        spot=1.1735,
        domestic_rate=0.042,
        foreign_rate=0.021,
    )

    assert market.pair == eurusd
    assert market.spot == 1.1735
    assert market.domestic_rate == 0.042
    assert market.foreign_rate == 0.021