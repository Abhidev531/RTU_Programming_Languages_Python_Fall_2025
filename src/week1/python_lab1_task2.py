"""
Task 2 – Greeting Function with String Manipulation
--------------------------------------------------
Write a function `greet_user(name)` that:
- removes extra spaces with .strip()
- capitalizes the first letter with .capitalize()
- returns "Hello, <Name>! Welcome to Python!"
Ask user for their name and print result.
"""


def greet_user(name):
    """Return a greeting message after cleaning and capitalizing the name."""
    name_clean = name.strip()
    name_formatted = name_clean.capitalize() if name_clean else ""
    if name_formatted:
        return f"Hello, {name_formatted}! Welcome to Python!"
    return "Hello! Welcome to Python!"


if __name__ == "__main__":
    name = input("Enter your name: ")
    print(greet_user(name))
