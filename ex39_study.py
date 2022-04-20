regions = {
    'marmara': 'istanbul',
    'central anatolia': 'ankara',
    'mediterranean': 'izmir'
}

cities = {
    'istanbul': 15_636_000,
    'ankara': 5_309_000,
}

cities['izmir'] = 3_056_000

print(f"Marmara region has {regions['marmara'].capitalize()}.")

print(
    f"The biggest city in Central Anatolia region is {regions['central anatolia'].title()}.")

print(
    f"Mediterranean region's biggest city has {cities[regions['mediterranean']]} population.")

print()
for region, city in regions.items():
    print(
        f"In {region.capitalize()} region biggest city is {city.capitalize()}.")

print()
for city, population in cities.items():
    print(f"{city.capitalize()} has {population} population.")

print()
for region, city in regions.items():
    print(f"In {region.title()} region biggest city is {city.capitalize()}")
    print(f"and its population is {cities[city]}.")

city = cities.get('bursa')

print(city)
