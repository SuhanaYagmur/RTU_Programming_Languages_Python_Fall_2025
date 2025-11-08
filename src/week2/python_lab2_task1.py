"""
Lab 3.1 — Simple Datasets and Aggregates

- Create and manipulate Python lists and dictionaries.
- Compute aggregates such as sum, average, max, and min.
"""

# --- 1) Datasets ---
# Example temperatures for 7 days (°C)
temperatures = [13.5, 15.2, 16.1, 14.8, 13.9, 12.7, 15.0]

# City populations (at least 5 cities)
city_population = {
    "Riga": 605_802,
    "Daugavpils": 80_652,
    "Liepaja": 68_645,
    "Jelgava": 55_726,
    "Jurmala": 49_675,
}

# --- 2) Aggregates ---
average_temperature = sum(temperatures) / len(temperatures) if temperatures else 0.0

# Largest and smallest cities by population
largest_city, largest_population = max(city_population.items(), key=lambda kv: kv[1])
smallest_city, smallest_population = min(city_population.items(), key=lambda kv: kv[1])

# Total population
total_population = sum(city_population.values())

# --- 3) Print results ---
print(f"Average temperature: {average_temperature:.2f} °C")
print(f"Largest city: {largest_city} - {largest_population:,}")
print(f"Smallest city: {smallest_city} - {smallest_population:,}")
print(f"Total population: {total_population:,}")
