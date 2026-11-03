# 1. T-Shirt Function (No spaces around '=' in default parameters)
def make_shirt(size='large', message='I love Python'):
    """Summarize the size and message of a t-shirt."""
    print(f"Making a {size} t-shirt with the message: '{message}'.")

# 2. City Names Function (Lowercase variables and function names with underscores)
def city_country(city, country):
    """Return a string formatted like 'City, Country'."""
    return f"{city.title()}, {country.title()}"

# 3. Cars Function (Descriptive names and standard docstrings)
def make_car(manufacturer, model, **options):
    """Store information about a car in a dictionary."""
    car_dict = {
        'manufacturer': manufacturer.title(),
        'model': model.title(),
    }
    for option, value in options.items():
        car_dict[option] = value
        
    return car_dict