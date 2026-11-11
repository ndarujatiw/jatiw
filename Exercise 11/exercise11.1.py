#city_functions.py
def city_country(city, country):
    """Return a string formatted as 'City, Country'."""
    return f"{city.title()}, {country.title()}"

#test_cities.py
from city_functions import city_country


def test_city_country():
    """Do cities like 'santiago, chile' work properly?"""
    santiago_chile = city_country("santiago", "chile")
    assert santiago_chile == "Santiago, Chile"
    
    #run in terminal
    #pytest
