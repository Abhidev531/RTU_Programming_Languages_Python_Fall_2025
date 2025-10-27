"""
Task 4 – Text-based Arithmetic Analyzer
--------------------------------------
Create a text-based analyzer that:
1. Counts non-space characters.
2. Counts words.
3. Extracts numbers and computes their sum and average.
Use helper functions:
- count_characters(text)
- count_words(text)
- extract_numbers(text)
- analyze_text(text)
Print formatted summary in main.
"""

import re
from typing import List, Optional, Tuple


def count_characters(text: str) -> int:
    """Count non-space characters in a string."""
    return sum(1 for ch in text if not ch.isspace())


def count_words(text: str) -> int:
    """Count number of words in a string."""
    words = re.findall(r"\b\w+\b", text)
    return len(words)


def extract_numbers(text: str) -> List[int]:
    """Return list of integers found in text."""
    nums = re.findall(r"-?\d+", text)
    return [int(n) for n in nums]


def analyze_text(text: str) -> Tuple[int, int, List[int], int, Optional[float]]:
    """Perform text-based arithmetic analysis.
    Returns (non_space_chars, word_count, numbers, total, average_or_None).
    """
    non_space_chars = count_characters(text)
    word_count = count_words(text)
    numbers = extract_numbers(text)
    total = sum(numbers) if numbers else 0
    average = (total / len(numbers)) if numbers else None
    return non_space_chars, word_count, numbers, total, average


if __name__ == "__main__":
    text = input("Enter text: ")
    chars, words, numbers, total, average = analyze_text(text)
    print(f"Non-space characters: {chars}")
    print(f"Word count: {words}")
    if numbers:
        print(f"Numbers found: {numbers}")
        print(f"Sum of numbers: {total}")
        print(f"Average of numbers: {average:.2f}")
    else:
        print("Numbers found: None")
        print("Sum of numbers: 0")
        print("Average of numbers: N/A")
