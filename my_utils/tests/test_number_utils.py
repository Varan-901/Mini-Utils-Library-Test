import pytest
from my_utils.number_utils import (
    clamp,
    is_prime,
    fibonacci,
    percentage,
)

# -----------------------
# clamp
# -----------------------

@pytest.mark.parametrize(
    "value,min_val,max_val,expected",
    [
        (5, 1, 10, 5),
        (-1, 0, 10, 0),
        (20, 0, 10, 10),
        (10, 0, 10, 10),
    ],
)
def test_clamp(value, min_val, max_val, expected):
    assert clamp(value, min_val, max_val) == expected


def test_clamp_invalid_range():
    with pytest.raises(ValueError):
        clamp(5, 10, 1)


# -----------------------
# is_prime
# -----------------------

@pytest.mark.parametrize(
    "n,expected",
    [
        (2, True),
        (3, True),
        (13, True),
        (9, False),
        (12, False),
        (1, False),
        (0, False),
        (-7, False),
        (100, False),
    ],
)
def test_is_prime(n, expected):
    assert is_prime(n) == expected


# -----------------------
# fibonacci
# -----------------------

@pytest.mark.parametrize(
    "n,expected",
    [
        (0, 0),
        (1, 1),
        (2, 1),
        (5, 5),
        (10, 55),
    ],
)
def test_fibonacci(n, expected):
    assert fibonacci(n) == expected


def test_fibonacci_negative():
    with pytest.raises(ValueError):
        fibonacci(-1)


# -----------------------
# percentage
# -----------------------

@pytest.mark.parametrize(
    "part,whole,expected",
    [
        (25, 100, 25.0),
        (1, 4, 25.0),
        (0, 10, 0.0),
        (-1, 10, -10.0),
        (2.5, 10, 25.0),
    ],
)
def test_percentage(part, whole, expected):
    assert percentage(part, whole) == expected


def test_percentage_zero_division():
    with pytest.raises(ZeroDivisionError):
        percentage(10, 0)