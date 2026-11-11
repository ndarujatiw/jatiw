class Restaurant:
    """A simple model of a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant name, cuisine type, and number served."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0  # Default value of 0

    def describe_restaurant(self):
        """Print the restaurant name and cuisine type."""
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")

    def open_restaurant(self):
        """Print a message indicating the restaurant is open."""
        print(f"{self.restaurant_name} is now open!")

    def set_number_served(self, number):
        """Set the number of customers that have been served."""
        self.number_served = number

    def increment_number_served(self, additional_customers):
        """Increment the number of customers who’ve been served."""
        self.number_served += additional_customers


# Create an instance called restaurant
restaurant = Restaurant("Bella Italia", "Italian")

# 1. Print initial number served
print(f"Initial customers served: {restaurant.number_served}")

# 2. Change value directly and print again
restaurant.number_served = 25
print(f"Updated directly: {restaurant.number_served}")

# 3. Use set_number_served() method
restaurant.set_number_served(75)
print(f"After set_number_served(75): {restaurant.number_served}")

# 4. Use increment_number_served() method (e.g., customers served in a day)
restaurant.increment_number_served(150)
print(f"After a busy day of service (+150): {restaurant.number_served}")