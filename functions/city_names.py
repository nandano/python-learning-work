def city_country(city, country):
    formatted_city = f"{city}, {country}"
    return formatted_city.title()

print(city_country('sao paolo', 'brazil'))
print(city_country('mumbai', 'india'))
print(city_country('oslo', 'norway'))