class Restaurant:
    """A simple model of a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant name and cuisine type attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Print the restaurant name and cuisine type."""
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")

    def open_restaurant(self):
        """Print a message indicating the restaurant is open."""
        print(f"{self.restaurant_name} is now open!")


# Create an instance of Restaurant
restaurant = Restaurant("Naspad Surya", "Naspad")

# Print attributes individually
print(f"Name attribute: {restaurant.restaurant_name}")
print(f"Cuisine attribute: {restaurant.cuisine_type}")

print()

# Call both methods
restaurant.describe_restaurant()
restaurant.open_restaurant()