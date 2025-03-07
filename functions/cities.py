def describe_city(city, country='norway'):
    print(f"{city.title()} is in {country.title()}.")

describe_city("mumbai", "india")
describe_city("oslo")
describe_city(country="usa", city="new york")