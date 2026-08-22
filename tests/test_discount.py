import pytest
from src.discount import apply_discount

def test_apply_valid_discount():
    assert apply_discount(100.0, "SAVE10") == 90.0
    assert apply_discount(200.0, "SAVE20") == 160.0
    assert apply_discount(50.0, "VIP50") == 25.0

def test_apply_unknown_coupon_should_not_crash():
    """Unknown coupon should apply 0% discount rather than raising KeyError."""
    assert apply_discount(100.0, "INVALID_CODE") == 100.0
    assert apply_discount(50.0, "") == 50.0

def test_price_should_never_be_negative():
    """Negative prices or excessive discounts should floor at 0.0."""
    assert apply_discount(-10.0, "SAVE10") == 0.0
