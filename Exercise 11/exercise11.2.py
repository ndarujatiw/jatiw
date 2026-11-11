#city_functions.py
def city_country(city, country, population=None):
    """Return a formatted string including population if provided."""
    if population:
        return f"{city.title()}, {country.title()} – population {population}"
    else:
        return f"{city.title()}, {country.title()}"
    
#test_cities.py
from city_functions import city_country


def test_city_country():
    """Test city and country formatting without population."""
    formatted_name = city_country("santiago", "chile")
    assert formatted_name == "Santiago, Chile"


def test_city_country_population():
    """Test city, country, and population formatting."""
    formatted_name = city_country("santiago", "chile", population=5000000)
    assert formatted_name == "Santiago, Chile – population 5000000"
    
#run pytest