class User:
    """A simple user profile model."""

    def __init__(self, first_name, last_name, username, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.location = location

    def describe_user(self):
        print(f"\nUser: {self.first_name} {self.last_name} (@{self.username})")
        print(f"  Email: {self.email}")
        print(f"  Location: {self.location}")

    def greet_user(self):
        print(f"Hello, {self.first_name}!")


class Privileges:
    """A separate class to store and display administrator privileges."""

    def __init__(self, privileges=None):
        if privileges is None:
            privileges = ["can add post", "can delete post", "can ban user"]
        self.privileges = privileges

    def show_privileges(self):
        """List the available privileges."""
        print("Administrator Privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")


class Admin(User):
    """Represent an administrator using a Privileges instance attribute."""

    def __init__(self, first_name, last_name, username, email, location):
        super().__init__(first_name, last_name, username, email, location)
        self.privileges = Privileges()


# Create an instance of Admin and use the Privileges method
admin_user = Admin("John", "Doe", "jdoe", "john@example.com", "Chicago")
admin_user.describe_user()
admin_user.privileges.show_privileges()