# Using the Restaurant class from Exercise 9-1
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


restaurant1 = Restaurant("Mieso Worth it", "Mieso")
restaurant2 = Restaurant("Nasgor Metro", "Nasgor")
restaurant3 = Restaurant("Kama", "Boneless Chicken")

# Call describe_restaurant() for each instance
restaurant1.describe_restaurant()
print()
restaurant2.describe_restaurant()
print()
restaurant3.describe_restaurant()