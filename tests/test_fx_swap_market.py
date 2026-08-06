from project_quant.fx_swap_quote import FXSwapQuote
from project_quant.fx_swap_market import FXSwapMarket
from project_quant.currency import CurrencyPair
import pytest

def test_mid():
    quote = FXSwapQuote(tenor="1M", bid=1.1730, ask=1.1735)
    assert quote.mid() == pytest.approx(1.17325)
def test_spread():
    quote = FXSwapQuote(tenor="1M", bid=1.1730, ask=1.1735)
    assert quote.spread() == pytest.approx(0.0005)
def test_add_quote():
    quote1 = FXSwapQuote(tenor="1M", bid=1.1730, ask=1.1735)
    quote2 = FXSwapQuote(tenor="3M", bid=1.1740, ask=1.1745)
    eurusd = CurrencyPair("EUR", "USD")
    market = FXSwapMarket(pair=eurusd, spot=1.1735, fx_swap_quotes=[quote1])
    market.add_quote(quote2)
    assert len(market.quotes()) == 2

def test_quote():
    quote1 = FXSwapQuote(tenor="1M", bid=1.1730, ask=1.1735)
    quote2 = FXSwapQuote(tenor="3M", bid=1.1740, ask=1.1745)
    eurusd = CurrencyPair("EUR", "USD")
    market = FXSwapMarket(pair=eurusd, spot=1.1735, fx_swap_quotes=[quote1, quote2])
    assert market.quote("1M") == quote1
    assert market.quote("3M") == quote2

def test_mid_points():
    quote1 = FXSwapQuote(tenor="1M", bid=1.1730, ask=1.1735)
    quote2 = FXSwapQuote(tenor="3M", bid=1.1740, ask=1.1745)
    eurusd = CurrencyPair("EUR", "USD")
    market = FXSwapMarket(pair=eurusd, spot=1.1735, fx_swap_quotes=[quote1, quote2])
    assert market.mid_points() == {"1M": 1.17325, "3M": 1.17425}