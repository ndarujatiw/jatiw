class Restaurant:
    """A simple model of a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")


class IceCreamStand(Restaurant):
    """Represent an ice cream stand, inheriting from Restaurant."""

    def __init__(self, restaurant_name, cuisine_type="ice cream"):
        """Initialize parent attributes and add an ice cream flavors attribute."""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = [
            "vanilla",
            "chocolate",
            "strawberry",
            "mint chocolate chip",
            "cookies and cream",
        ]

    def display_flavors(self):
        """Display the available ice cream flavors."""
        print(f"\nAvailable flavors at {self.restaurant_name}:")
        for flavor in self.flavors:
            print(f"- {flavor.title()}")


# Create an instance of IceCreamStand and call the method
ice_cream_stand = IceCreamStand("Scoops & Smiles")
ice_cream_stand.describe_restaurant()
ice_cream_stand.display_flavors()