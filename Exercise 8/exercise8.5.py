def describe_city(city, country='England'):
    """Describe the country a city is in."""
    print(f"{city.title()} is in {country.title()}.")

# Two cities in the default country
describe_city('London')
describe_city('Manchester')

# One city not in the default country
describe_city('Solo', country='Indonesia')