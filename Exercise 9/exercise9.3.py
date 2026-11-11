class User:
    """A class representing a user profile."""

    def __init__(self, first_name, last_name, username, email, location):
        """Initialize user attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.location = location

    def describe_user(self):
        """Print a summary of the user's information."""
        full_name = f"{self.first_name} {self.last_name}"
        print(f"User Profile: {full_name}")
        print(f"  Username: {self.username}")
        print(f"  Email: {self.email}")
        print(f"  Location: {self.location}")

    def greet_user(self):
        """Print a personalized greeting to the user."""
        print(f"Welcome back, {self.first_name}!")


# Create several user instances
user1 = User("Ndaru", "Jati", "Jatiw", "jatiw@example.com", "Jebres")
user2 = User("Bob", "Jones", "b_jones", "bob@example.com", "London")
user3 = User("Carla", "Mendoza", "cmendoza", "carla@example.com", "Madrid")

# Call describe_user() and greet_user() for each user
users = [user1, user2, user3]

for user in users:
    user.describe_user()
    user.greet_user()
    print()