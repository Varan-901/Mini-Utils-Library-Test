import math


def clamp(value, min_val, max_val):
    if min_val > max_val:
        raise ValueError("min_val cannot be greater than max_val")

    return max(min_val, min(value, max_val))


def is_prime(n):
    if n <= 1:
        return False

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    for i in range(3, math.isqrt(n) + 1, 2):
        if n % i == 0:
            return False

    return True


def fibonacci(n):
    if n < 0:
        raise ValueError("n cannot be negative")

    if n == 0:
        return 0

    if n == 1:
        return 1

    a, b = 0, 1

    for _ in range(2, n + 1):
        a, b = b, a + b

    return b


def percentage(part, whole):
    if whole == 0:
        raise ZeroDivisionError("whole cannot be zero")

    return (part / whole) * 100
