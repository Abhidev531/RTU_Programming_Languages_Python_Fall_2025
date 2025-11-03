"""
Lab 3.1 – Simple Datasets and Aggregates

Goals:
- Create and manipulate Python lists and dictionaries.
- Compute aggregates such as sum, average, max, and min.

Instructions:
1. Create a list `temperatures` with daily temperatures for one week.
2. Create a dictionary `city_population` with at least 5 cities and their populations.
3. Compute:
   - The average temperature.
   - The maximum and minimum population.
   - The total population of all cities.
4. Print your results in a clear, formatted way.
"""

# TODO: Create the datasets - up to you to fill in the data
temperatures = [22.5, 24.0, 19.8, 21.0, 23.3, 25.1, 20.4]

city_population = {
    "Riga": 632614,
    "Daugavpils": 83690,
    "Liepaja": 74020,
    "Jelgava": 54000,
    "Valmiera": 25600,
}

# TODO: Compute aggregates
average_temperature = None
if temperatures:
    average_temperature = sum(temperatures) / len(temperatures)

total_population = sum(city_population.values()) if city_population else 0

if city_population:
    largest_city, largest_population = max(
        city_population.items(), key=lambda kv: kv[1]
    )
    smallest_city, smallest_population = min(
        city_population.items(), key=lambda kv: kv[1]
    )
else:
    largest_city, largest_population = "", 0
    smallest_city, smallest_population = "", 0

# TODO: Print results
print(f"Temperatures (week): {temperatures}")
if average_temperature is not None:
    print(f"Average temperature: {average_temperature:.2f} °C")
else:
    print("Average temperature: N/A")

print(f"Largest city: {largest_city} - {largest_population}")
print(f"Smallest city: {smallest_city} - {smallest_population}")
print(f"Total population: {total_population}")
