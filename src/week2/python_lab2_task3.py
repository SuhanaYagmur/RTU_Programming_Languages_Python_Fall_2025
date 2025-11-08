"""
Lab 3.3 — Operator Frequency Counter

Idea:
Ask the user for an arithmetic expression and count how many times each operator
appears. We’ll keep the counts in a dictionary.
"""

def count_operators(expr: str) -> dict:
    # I only care about these characters as "operators"
    operators = ['+', '-', '*', '/', '(', ')']

    # Start every operator at 0 so the result always shows all keys
    counts = {op: 0 for op in operators}

    # Go through every character; if it is one of the operators, increase its count
    for ch in expr:
        if ch in counts:
            counts[ch] += 1

    return counts


if __name__ == "__main__":
    # 1) Get input from the user
    expression = input("Enter an arithmetic expression (e.g., 3 + 5 * (2 - 1)): ")

    # 2) Count operators
    operator_counts = count_operators(expression)

    # 3) Print results in a clear way
    print("\nOperator counts:")
    for op in ['+', '-', '*', '/', '(', ')']:  # fixed order for nice output
        print(f"  {op}: {operator_counts[op]}")
