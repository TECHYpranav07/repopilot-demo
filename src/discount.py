"""
Discount and Coupon Calculation Module.
"""

COUPON_RATES = {
    "SAVE10": 0.10,
    "SAVE20": 0.20,
    "VIP50": 0.50,
}

def calculate_discount_amount(price: float, rate: float) -> float:
    return price * rate

def apply_discount(price: float, coupon_code: str) -> float:
    """
    Applies a percentage discount to the price using the specified coupon code.

    Bugs:
    1. If an unknown coupon_code is passed, it raises KeyError instead of 0.0 discount.
    2. If price is negative or discount exceeds price, final price should not be negative.
    """
    # Bug: Directly indexing dictionary causes KeyError on unknown coupons
    rate = COUPON_RATES[coupon_code]
    discount = calculate_discount_amount(price, rate)
    return price - discount
