"""
Lab 3.4 — Functional Tools Practice

Goal:
Practice `map`, `filter`, and `zip`, and compare them with list comprehensions.
"""

# Given data (same length, so zip will pair them correctly)
prices = [12.5, 9.9, 15.0, 22.3, 5.0]
quantities = [2, 5, 1, 3, 4]

# --- Using functional tools ---

# totals: for each (price, qty) I multiply them -> total cost per item
# I zip first to get pairs, then map with a lambda to multiply
totals = list(map(lambda pq: pq[0] * pq[1], zip(prices, quantities)))

# high_totals: I only keep totals that are strictly greater than 30
high_totals = list(filter(lambda t: t > 30, totals))

# pairs: just to show the raw (price, qty) pairs using zip
pairs = list(zip(prices, quantities))

# --- Using list comprehensions (same results, just a different style) ---

# Do the same multiplication but with a comprehension
totals_comp = [p * q for p, q in zip(prices, quantities)]

# Same filtering logic with a comprehension
high_totals_comp = [t for t in totals_comp if t > 30]

# --- Print results nicely ---
print("Prices:", prices)
print("Quantities:", quantities)
print("Pairs (price, qty):", pairs)
print("Totals:", [round(x, 2) for x in totals])
print("Totals > 30:", [round(x, 2) for x in high_totals])
print("Totals (comprehension):", [round(x, 2) for x in totals_comp])
print("Totals > 30 (comprehension):", [round(x, 2) for x in high_totals_comp])
