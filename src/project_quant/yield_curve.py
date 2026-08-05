class YieldCurve:
    def __init__(self, discount_factors: dict[float, float]):
        if not discount_factors:
            raise ValueError("Discount factors dictionary cannot be empty.")
        if any(discount_factor <= 0 for discount_factor in discount_factors.values()):
            raise ValueError("All discount factors must be positive.")
        if any(maturity <= 0 for maturity in discount_factors.keys()):
            raise ValueError("All maturities must be positive.")
        self.discount_factors = discount_factors
    def discount_factor(self, maturity:float) -> float:
        """
        Get the discount factor for a given maturity.

        Parameters
        ----------
        maturity : float

        Returns
        -------
        float
            The discount factor for the given maturity.
        """
        if maturity <= 0:
            raise ValueError("Maturity must be positive.")
        if maturity not in self.discount_factors:
            raise ValueError(f"No discount factor available for maturity {maturity}.")
        return self.discount_factors[maturity]
    def rate(self, maturity: float) -> float:
        """
        Get the interest rate for a given maturity.

        Parameters
        ----------
        maturity : float

        Returns
        -------
        float
            The interest rate for the given maturity.
        """
        if maturity <= 0:
            raise ValueError("Maturity must be positive.")
        if maturity not in self.discount_factors:
            raise ValueError(f"No discount factor available for maturity {maturity}.")
        discount_factor = self.discount_factor(maturity)
        rate = (1 / discount_factor - 1) / maturity
        return rate
    def has_tenor(self, maturity: float) -> bool:
        """
        Check if the yield curve has a discount factor for the given maturity.

        Parameters
        ----------
        maturity : float

        Returns
        -------
        bool
            True if the yield curve has a discount factor for the given maturity, False otherwise.
        """
        if maturity <= 0:
            raise ValueError("Maturity must be positive.")
        return maturity in self.discount_factors
    def tenors(self) -> list[float]:
        """
        Get the list of maturities (tenors) for which discount factors are available.

        Returns
        -------
        list[float]
            The list of maturities (tenors).
        """
        return sorted(self.discount_factors.keys())
    