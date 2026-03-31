"""
Calculate pi to a specified number of decimal places using the Chudnovsky algorithm.
Usage: python calculate_pi.py [digits]
Default: 50 digits
"""

import sys
from decimal import Decimal, getcontext
import math


def chudnovsky_pi(digits: int) -> Decimal:
    """
    Compute pi to the given number of decimal digits using the Chudnovsky algorithm.
    Each iteration adds ~14.18 correct decimal digits.
    """
    # Set precision high enough to avoid rounding errors
    getcontext().prec = digits + 20

    C = 426880 * Decimal(10005).sqrt()
    M = Decimal(1)
    X = Decimal(1)
    K = Decimal(6)
    S = Decimal(13591409)
    L = Decimal(13591409)

    for i in range(1, math.ceil(digits / 14) + 5):
        M = M * (K ** 3 - 16 * K) / (i ** 3)
        X *= -262537412640768000
        L += 545140134
        S += M * L / X
        K += 12

    pi = C / S
    # Truncate to requested precision
    getcontext().prec = digits + 2
    return +pi  # re-round to current precision


def main():
    digits = int(sys.argv[1]) if len(sys.argv) > 1 else 50

    if digits < 1:
        print("Digits must be a positive integer.")
        sys.exit(1)

    print(f"Computing pi to {digits} decimal places...\n")
    pi = chudnovsky_pi(digits)

    # Format: trim to exactly `digits` decimal places
    pi_str = str(pi)
    # Ensure we show exactly `digits` decimal places
    if '.' in pi_str:
        integer_part, decimal_part = pi_str.split('.')
        decimal_part = (decimal_part + '0' * digits)[:digits]
        pi_str = f"{integer_part}.{decimal_part}"

    print(f"pi = {pi_str}")


if __name__ == "__main__":
    main()
