cities = {
    'mumbai': {'country': 'india', 'population': 18000000, 'fact': 'also known as the city of dreams'},
    'bangalore': {'country': 'india', 'population': 13000000, 'fact': 'also known as the tech capital of india'},
    'new york': {'country': 'usa', 'population': 8000000, 'fact': 'the most populous city in the usa'},
}

for city in cities:
    print(f"\nCity: {city}\n")
    for info_title, info in cities[city].items():
        print(f"\t{info_title}: {info}")