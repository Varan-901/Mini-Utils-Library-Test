def truncate(text, max_len):
    if text is None:
        raise ValueError("text cannot be None")

    if max_len < 0:
        raise ValueError("max_len cannot be negative")

    if len(text) <= max_len:
        return text

    if max_len <= 3:
        return "." * max_len

    return text[: max_len - 3] + "..."


def title_case(text):
    if text is None:
        raise ValueError("text cannot be None")

    return text.title()


def is_palindrome(text):
    if text is None:
        raise ValueError("text cannot be None")

    cleaned = "".join(text.lower().split())
    return cleaned == cleaned[::-1]


def count_vowels(text):
    if text is None:
        raise ValueError("text cannot be None")

    vowels = "aeiou"
    return sum(1 for char in text.lower() if char in vowels)
