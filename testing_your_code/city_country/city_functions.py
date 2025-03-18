def city_country(city, country, population=None):
    """Return a neatly formatted city name along with the country."""
    if population:
        formatted_city = f"{city.title()}, {country.title()} - population {population}"
    else:
        formatted_city = f'{city}, {country}'.title()
    return formatted_city