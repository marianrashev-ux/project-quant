from project_quant.currency import CurrencyPair
from project_quant.fx_swap_quote import FXSwapQuote

class FXSwapMarket:
    def __init__(self, pair: CurrencyPair, spot: float, fx_swap_quotes: list[FXSwapQuote]):
        if not fx_swap_quotes:
            raise ValueError("FX swap quotes list cannot be empty.")
        if spot <= 0:
            raise ValueError("Spot rate must be positive.")
        self.fx_swap_quotes = fx_swap_quotes
        self.pair = pair
        self.spot = spot
    def quotes(self) -> list[FXSwapQuote]:
        """
        Get the list of FX swap quotes.

        Returns
        -------
        list[FXSwapQuote]
            The list of FX swap quotes.
        """
        return self.fx_swap_quotes
    def add_quote(self, quote: FXSwapQuote):
        """
        Add a new FX swap quote to the market.

        Parameters
        ----------
        quote : FXSwapQuote
            The FX swap quote to add.
        """
        for existing in self.fx_swap_quotes:
            if existing.tenor == quote.tenor:
                raise ValueError(f"Quote for tenor {quote.tenor} already exists.")
        self.fx_swap_quotes.append(quote)
    def quote(self, tenor: str) -> FXSwapQuote:
        """
        Get the FX swap quote for a specific tenor.

        Parameters
        ----------
        tenor : str
            The tenor for which to get the FX swap quote.

        Returns
        -------
        FXSwapQuote
            The FX swap quote for the specified tenor.

        Raises
        ------
        ValueError
            If no quote is found for the specified tenor.
        """
        for quote in self.fx_swap_quotes:
            if quote.tenor == tenor:
                return quote
        raise ValueError(f"No quote found for tenor: {tenor}")
    def mid_points(self) -> dict[str, float]:
        """
        Get the mid points for all FX swap quotes in the market.

        Returns
        -------
        dict[str, float]
            A dictionary with tenors as keys and mid points as values.
        """
        return {quote.tenor: quote.mid() for quote in self.fx_swap_quotes}
    def str(self) -> str:
        """
        Get a string representation of the FX swap market.

        Returns
        -------
        str
            A string representation of the FX swap market.
        """
        quotes_str = "\n".join(str(quote) for quote in self.fx_swap_quotes)
        return f"FX Swap Market for {self.pair}:\nSpot: {self.spot}\nQuotes:\n{quotes_str}"