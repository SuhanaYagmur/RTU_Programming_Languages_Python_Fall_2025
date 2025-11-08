"""
Lab 3.2 — Comprehensions and Transformations

Goal:
Practice list, set, and dictionary comprehensions to transform and filter data quickly.
"""

# 1) Base dataset (I can change this later if I want)
numbers = [3, 8, -2, 7, 0, -5, 10]

if __name__ == "__main__":
    # If I press 'r', I’ll generate 10 random integers just to test the code on new data.
    choice = input("Press 'r' to generate 10 random integers, or Enter to keep default: ").strip().lower()
    if choice == "r":
        import random
        random.seed(42)  # fixed seed so results are reproducible
        numbers = [random.randint(-10, 10) for _ in range(10)]

# 2) Comprehensions
# squares: list that holds n^2 for every n (I’m transforming each element)
squares = [n * n for n in numbers]

# positives: list that keeps only numbers > 0 (I’m filtering)
positives = [n for n in numbers if n > 0]

# even_squares: set of squares but only for even numbers (filter + square, set removes duplicates)
even_squares = {n * n for n in numbers if n % 2 == 0}

# cubes: dictionary that maps each number to its cube (key = n, value = n^3)
cubes = {n: n ** 3 for n in numbers}

# 3) Print results in a clear way
print("Numbers:", numbers)
print("Squares:", squares)
print("Positives:", positives)
print("Even squares:", even_squares)
print("Cubes:", cubes)
