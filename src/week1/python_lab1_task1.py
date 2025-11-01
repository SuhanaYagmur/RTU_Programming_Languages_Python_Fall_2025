import math
import random

def circle_area(radius):
    """Return the area of a circle given its radius."""
    return math.pi * (radius ** 2)

if __name__ == "__main__":
    # Marjinal (uç) test değerleri
    test_values = [0, 0.0001, 1, 999999, -5, random.uniform(-1000, 1000)]

    for r in test_values:
        try:
            if r < 0:
                print(f"Radius {r}: invalid (negative radius)")
            else:
                area = circle_area(r)
                print(f"Radius {r} -> Area: {area:.2f}")
        except Exception as e:
            print(f"Radius {r} -> Error: {e}")
