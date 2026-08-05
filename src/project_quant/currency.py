class CurrencyPair:
    def __init__(self, base_currency: str, quote_currency: str):
        if(len(base_currency) != 3 or len(quote_currency) != 3):
            raise ValueError("Currency codes must be 3 characters long.")
        if(base_currency == quote_currency):
            raise ValueError("Base and quote currencies must be different.")
        base_currency = base_currency.upper()
        quote_currency = quote_currency.upper()
        self.base_currency = base_currency
        self.quote_currency = quote_currency
    def __str__(self):
        return f"{self.base_currency}/{self.quote_currency}"
    def contains(self, currency: str) -> bool:
        """
        Check if the currency pair contains the given currency.

        Parameters
        ----------
        currency : str

        Returns
        -------
        bool
        """
        currency = currency.upper()
        if(len(currency) != 3):
            raise ValueError("Currency code must be 3 characters long.")
        return currency == self.base_currency or currency == self.quote_currency