# My Utils

<b>A simple Python utility library built for performing simple number and string actions.</b><br><br>
This is a project created with the purpose of learning Test-Driven Development (TDD), unit testing with pytest, package creation and understanding code coverage analysis.<br><br>
_(Created for Software Engineering Course, May 2026)_

## Project Structure

```text
.
├── my_utils/
│   ├── __init__.py
│   ├── string_utils.py
│   └── number_utils.py
├── tests/
│   ├── test_string_utils.py
│   └── test_number_utils.py
└── venv/
```

## Features

### String Utilities

- `truncate(text, max_len)`  
  Truncates text and adds "..." if needed.

- `title_case(text)`  
  Converts text to title case.

- `is_palindrome(text)`  
  Checks if text is a palindrome (ignores spaces and case).

- `count_vowels(text)`  
  Counts the number of vowels in a string.

---

### Number Utilities

- `clamp(value, min_val, max_val)`  
  Clamps a number within a specified range.

- `is_prime(n)`  
  Returns `True` if the number is prime.

- `fibonacci(n)`  
  Returns the nth Fibonacci number.

- `percentage(part, whole)`  
  Returns the percentage value.

## Setup
Install dependencies:
```bash
pip install -r requirements.txt
#Or manually:
pip install pytest pytest-cov

#Running Tests
#- Run all tests:
python -m pytest

#Code Coverage
#- Run tests with coverage:
python -m pytest --cov=my_utils --cov-report=term-missing

#Goal: at least 95% coverage
----------------------------
#Example Usage
from my_utils.string_utils import truncate, is_palindrome from my_utils.number_utils import fibonacci, percentage

print(truncate("hello world", 8)) print(is_palindrome("racecar")) print(fibonacci(10)) print(percentage(25, 100))
```
### NOTES:
- Always run commands from the project root
- Do not run files inside the my_utils folder directly
- Use python -m pytest if pytest command does not work on Windows
