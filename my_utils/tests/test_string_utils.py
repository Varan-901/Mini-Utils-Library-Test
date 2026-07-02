import pytest
from my_utils.string_utils import (
    truncate,
    title_case,
    is_palindrome,
    count_vowels,
)

# -----------------------
# truncate
# -----------------------

@pytest.mark.parametrize(
    "text,max_len,expected",
    [
        ("hello world", 8, "hello..."),
        ("hello", 10, "hello"),
        ("abcd", 4, "abcd"),
        ("hello", 2, ".."),
        ("", 5, ""),
    ],
)
def test_truncate(text, max_len, expected):
    assert truncate(text, max_len) == expected


@pytest.mark.parametrize("text,max_len", [(None, 5), ("hello", -1)])
def test_truncate_errors(text, max_len):
    with pytest.raises(ValueError):
        truncate(text, max_len)


# -----------------------
# title_case
# -----------------------

@pytest.mark.parametrize(
    "text,expected",
    [
        ("hello world", "Hello World"),
        ("", ""),
    ],
)
def test_title_case(text, expected):
    assert title_case(text) == expected


def test_title_case_none():
    with pytest.raises(ValueError):
        title_case(None)


# -----------------------
# palindrome
# -----------------------

@pytest.mark.parametrize(
    "text,expected",
    [
        ("racecar", True),
        ("Race car", True),
        ("hello", False),
        ("", True),
        ("nurses run", True),
    ],
)
def test_is_palindrome(text, expected):
    assert is_palindrome(text) == expected


def test_is_palindrome_none():
    with pytest.raises(ValueError):
        is_palindrome(None)


# -----------------------
# vowels
# -----------------------

@pytest.mark.parametrize(
    "text,expected",
    [
        ("hello", 2),
        ("AEIOU", 5),
        ("rhythm", 0),
        ("", 0),
    ],
)
def test_count_vowels(text, expected):
    assert count_vowels(text) == expected


def test_count_vowels_none():
    with pytest.raises(ValueError):
        count_vowels(None)