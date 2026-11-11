#restaurant.py
class Restaurant:
    """A simple model of a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")
        
#my_restaurant.py
from restaurant import Restaurant

# Create an instance and call a method
favorite_restaurant = Restaurant("Sakura Sushi", "Japanese")
favorite_restaurant.describe_restaurant()
favorite_restaurant.open_restaurant()