import math
def calculate_arithmetic_returns(prices: list[float]) -> list[float]:
    """
    Calculate arithmetic returns from a sequence of prices.

    Parameters
    ----------
    prices : list[float]

    Returns
    -------
    list[float]
    """
    if (len(prices) < 2):
        raise ValueError("At least two prices are required to calculate returns.")
    arithmetic_returns = []
    for i in range(1, len(prices)):
        return_value = (prices[i] - prices[i-1]) / prices[i-1]
        arithmetic_returns.append(return_value)
    return arithmetic_returns
def calculate_log_returns(prices: list[float]) -> list[float]:
    """
    Calculate log returns from a sequence of prices.

    Parameters
    ----------
    prices : list[float]

    Returns
    -------
    list[float]
    """
    if len(prices) <2:
       raise ValueError("At least two prices are required to calculate returns.")
    log_returns = []
    for i in range(1, len(prices)):
       return_value = math.log(prices[i] / prices[i - 1])
       log_returns.append(return_value)
    return log_returns
def calculate_average_return(returns: list[float]) -> float:
    """
    Calculate the average return from a sequence of returns.

    Parameters
    ----------
    returns : list[float]

    Returns
    -------
    float
    """
    if len(returns) == 0:
        raise ValueError("At least one return is required to calculate average return.")
    average_return = sum(returns) / len(returns)
    return average_return
def calculate_cumulative_return(prices: list[float]) -> float:
    """
    Calculate the cumulative return from a sequence of prices.

    Parameters
    ----------
    prices : list[float]

    Returns
    -------
    float
    """
    if len(prices) < 2:
        raise ValueError("At least two prices are required to calculate cumulative return.")
    first_price = prices[0]
    last_price = prices[-1]
    cumulative_return = (last_price - first_price) / first_price
    return cumulative_return