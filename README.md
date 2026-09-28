# Discount and Coupon Calculation Module

This project provides a Python module for calculating discounts and applying coupon codes to prices. It also includes a simple `greet` function to generate personalized greeting messages.

## Features
- Apply discounts using predefined coupon codes.
- Ensure prices never go negative after applying discounts.
- Generate greeting messages for any name.

## Usage

### Applying Discounts
Use the `apply_discount` function to calculate the final price after applying a coupon code:
```python
from src.discount import apply_discount

price = 100.0
coupon_code = "SAVE10"
final_price = apply_discount(price, coupon_code)
print(final_price)  # Output: 90.0
```

### Generating Greetings
Use the `greet` function to generate a greeting message:
```python
from src.discount import greet

name = "Alice"
message = greet(name)
print(message)  # Output: "Hello, Alice!"
```

## Acknowledgments
Special thanks to [User's Name] for their contribution to this project!
