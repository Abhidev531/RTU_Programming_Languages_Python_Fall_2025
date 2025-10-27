"""
Task 1 – Simple Function with Arithmetic
---------------------------------------
Write a function `circle_area(radius)` that returns the area of a circle.
Formula: area = π × radius²
Use the math module for π.
Ask user for radius and print result with 2 decimals.
"""

import math


def circle_area(radius):
    """Return the area of a circle given its radius."""
    return math.pi * (radius**2)


if __name__ == "__main__":
    try:
        radius_str = input("Enter radius: ").strip()
        radius = float(radius_str)
        if radius < 0:
            raise ValueError("Radius must be non-negative.")
    except ValueError as e:
        print(f"Invalid input: {e}")
    else:
        area = circle_area(radius)
        print(f"Area: {area:.2f}")
