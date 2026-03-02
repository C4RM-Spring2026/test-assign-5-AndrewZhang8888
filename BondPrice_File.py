import numpy as np

def getBondPrice(y, face, couponRate, m, ppy=1):
    n = m * ppy
    y_period = y / ppy
    coupon = face * couponRate / ppy
    periods = np.arange(1, n + 1)
    cash_flows = np.full(n, coupon)
    cash_flows[-1] += face  
    discount_factors = (1 + y_period) ** periods
    pv_cash_flows = cash_flows / discount_factors
    price = np.sum(pv_cash_flows)
    return price
