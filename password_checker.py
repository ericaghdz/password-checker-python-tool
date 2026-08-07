"""
Password Strength Checker
Evaluates a password against basic strength rules (length, digit,
uppercase letter) and reports an overall strength rating.
"""


class PasswordChecker:
    """Evaluates the strength of a single password."""

    def __init__(self, password):
        self.password = password

    def check_length(self):
        """Returns True if the password is at least 8 characters long."""
        return len(self.password) >= 8

    def check_has_digit(self):
        """Returns True if the password contains at least one digit."""
        has_digit = False
        for character in self.password:
            if character.isdigit():
                has_digit = True
        return has_digit

    def check_has_upper(self):
        """Returns True if the password contains at least one uppercase letter."""
        has_upper = False
        for character in self.password:
            if character.isupper():
                has_upper = True
        return has_upper

    def strength(self):
        """
        Returns an overall strength rating: "Strong", "Medium", or "Weak".

        Strong: meets length, digit, and uppercase requirements.
        Medium: meets length only.
        Weak: fails the length requirement.
        """
        if self.check_length() and self.check_has_digit() and self.check_has_upper():
            return "Strong"
        elif self.check_length():
            return "Medium"
        else:
            return "Weak"


if __name__ == "__main__":
    password = input("Enter a password to check: ")
    checker = PasswordChecker(password)
    print("Password strength:", checker.strength())
