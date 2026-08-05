from project_quant.currency import CurrencyPair

class FXForward:
    def __init__(
            self,
            pair: CurrencyPair,
            spot: float,
            domestic_rate: float,
            foreign_rate: float,
            maturity: float
    ):
        if spot<=0:
            raise ValueError("Spot rate must be positive.")
        if maturity<=0:
            raise ValueError("Maturity must be positive.")
        self.pair = pair
        self.spot = spot
        self.domestic_rate = domestic_rate
        self.foreign_rate = foreign_rate
        self.maturity = maturity
    def price(self) -> float:
        """
        Calculate the price of the FX forward contract.

        Returns
        -------
        float
            The price of the FX forward contract.
        """
        forward_price = self.spot * (
            (1 + self.domestic_rate * self.maturity) 
            / (1 + self.foreign_rate * self.maturity)
        )
        return forward_price