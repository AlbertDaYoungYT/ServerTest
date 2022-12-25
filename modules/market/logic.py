from config import *
import matplotlib.pyplot as plt
import numpy as np
from math import *


def calculate_market_price(supply: int, demand: int, base_price) -> float:
    """
    Calculates the market price of an item based on supply and demand.
    
    Parameters:
    supply (int): The amount of the item that is currently available in the market.
    demand (int): The demand for the item in the market.
    base_price (float): The base price of the item.
    
    Returns:
    float: The market price of the item.
    """
    # If there is a surplus of supply, the price will decrease
    if supply > demand:
        return base_price * (1 - 0.05 * (supply - demand) / demand)
    # If there is a shortage of supply, the price will increase
    elif demand > supply:
        return base_price * (1 + 0.05 * (demand - supply) / supply)
    # If there is a balance of supply and demand, the price will remain the same
    else:
        return base_price



market_price = calculate_market_price(supply=100, demand=100, base_price=100)

print(market_price)
