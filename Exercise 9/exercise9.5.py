class User:
    """A class representing a user profile."""

    def __init__(self, first_name, last_name, username, email, location):
        """Initialize user attributes, including login attempts."""
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.location = location
        self.login_attempts = 0  # Default value of 0

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

    def increment_login_attempts(self):
        """Increment the value of login_attempts by 1."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset the value of login_attempts to 0."""
        self.login_attempts = 0


# Make an instance of the User class
user = User("Alice", "Smith", "asmith", "alice@example.com", "New York")

# Call increment_login_attempts() several times
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()

# Print login_attempts to make sure it was incremented properly
print(f"Login attempts after failed logins: {user.login_attempts}")

# Call reset_login_attempts()
user.reset_login_attempts()

# Print login_attempts again to make sure it was reset to 0
print(f"Login attempts after reset: {user.login_attempts}")