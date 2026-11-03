def city_country(city, country):
    """Return a string formatted like 'City, Country'."""
    return f"{city.title()}, {country.title()}"

print(city_country('venice', 'italia'))
print(city_country('tokyo', 'jepang'))
print(city_country('paris', 'francis'))