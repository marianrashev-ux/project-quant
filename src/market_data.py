from currency import CurrencyPair

class MarketData:
    def __init__(
            self, 
            pair: CurrencyPair,
            spot: float,
            domestic_rate: float,
            foreign_rate: float
    ):
        self.pair = pair
        self.spot = spot
        self.domestic_rate = domestic_rate
        self.foreign_rate = foreign_rate
        if spot <= 0:
            raise ValueError("Spot rate must be positive.")
    def __str__(self):
        return f"MarketData({self.pair}, Spot: {self.spot}, Domestic Rate: {self.domestic_rate}, Foreign Rate: {self.foreign_rate})"
