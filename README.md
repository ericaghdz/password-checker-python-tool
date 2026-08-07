# Password Strength Checker

A small Python tool that evaluates a password against basic strength rules and returns an overall rating — built as an object-oriented practice project, modeling each password as a `PasswordChecker` object with its own data and checks.

## What it does

Given a password, the tool checks:
- **Length** — at least 8 characters
- **Digit** — contains at least one number
- **Uppercase** — contains at least one uppercase letter

...and returns an overall rating:

```
"cat"        -> Weak    (fails length)
"sunshine"   -> Medium  (passes length only)
"Sunshine1"  -> Strong  (passes all three checks)
```

## How it works

```python
class PasswordChecker:
    def __init__(self, password):
        self.password = password

    def check_length(self):
        return len(self.password) >= 8

    def check_has_digit(self):
        has_digit = False
        for character in self.password:
            if character.isdigit():
                has_digit = True
        return has_digit

    def check_has_upper(self):
        has_upper = False
        for character in self.password:
            if character.isupper():
                has_upper = True
        return has_upper

    def strength(self):
        if self.check_length() and self.check_has_digit() and self.check_has_upper():
            return "Strong"
        elif self.check_length():
            return "Medium"
        else:
            return "Weak"
```

- `__init__` stores the password on the object itself (`self.password`), so every method below can access it without needing it passed in again.
- Each `check_*` method loops through the password character by character, checking a single property, and returns `True` or `False`.
- `strength()` calls the other methods on the same object (`self.check_length()`, etc.) and combines their results into one overall rating.

## Usage

```bash
python password_checker.py
```

Or use it directly in code:

```python
from password_checker import PasswordChecker

checker = PasswordChecker("Sunshine1")
print(checker.strength())        # "Strong"
print(checker.check_length())    # True
print(checker.check_has_digit()) # True
print(checker.check_has_upper()) # True
```

Each `PasswordChecker` object is independent — creating one for a different password doesn't affect any others, since each stores its own `self.password`.

## Possible next steps

- Add a check for special characters (`!`, `@`, `#`, etc.)
- Check against a list of common weak passwords
- Return a numeric score instead of just Strong/Medium/Weak, for finer-grained feedback
- Add a `suggestions()` method that explains exactly what's missing for a weak or medium password

## Background

Built as a second object-oriented practice project, following the same file-driven `LoginAttempt`/log-parser project — deliberately revisiting the same core concepts (input, conditionals, loops, functions, classes) on a new problem to reinforce retention.
