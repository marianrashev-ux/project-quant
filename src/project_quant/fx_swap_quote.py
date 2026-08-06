class FXSwapQuote:
    def __init__(
        self,
        tenor: str,
        bid: float,
        ask: float,
    ):
        if bid >= ask:
            raise ValueError("Bid price must be less than ask price.")
        if not tenor:
            raise ValueError("Tenor cannot be empty.")
        self.tenor = tenor
        self.bid = bid
        self.ask = ask
    def mid(self) -> float:
        """
        Calculate the mid price of the FX swap quote.

        Returns
        -------
        float
            The mid price of the FX swap quote.
        """
        return (self.bid + self.ask) / 2
    def spread(self) -> float:
        """
        Calculate the spread of the FX swap quote.

        Returns
        -------
        float
            The spread of the FX swap quote.
        """
        return self.ask - self.bid
    def __str__(self):
        return (
        f"{self.tenor}: "
        f"{self.bid} / {self.ask} "
        f"(mid: {self.mid():.4f})"
        )
    