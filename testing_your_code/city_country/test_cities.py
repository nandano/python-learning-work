from city_functions import city_country

def test_city_country():
    """Do inputs like Santiago, Chile work?"""
    formatted_city = city_country('santiago', 'chile')
    assert formatted_city == 'Santiago, Chile'

def test_city_country_population():
    """Do inputs like Santiago, Chile - population 5000000 work?"""
    formatted_city = city_country('santiago', 'chile', 5000000)
    assert formatted_city == 'Santiago, Chile - population 5000000'