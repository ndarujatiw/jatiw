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


class Admin(User):
    """Represent an administrator user profile."""

    def __init__(self, first_name, last_name, username, email, location):
        """Initialize parent attributes and add administrator privileges."""
        super().__init__(first_name, last_name, username, email, location)
        self.privileges = [
            "can add post",
            "can delete post",
            "can ban user",
            "can modify site settings",
        ]

    def show_privileges(self):
        """List the administrator's privileges."""
        print(f"\nPrivileges for Admin {self.first_name} {self.last_name}:")
        for privilege in self.privileges:
            print(f"- {privilege}")


# Create an instance of Admin and call show_privileges()
admin_user = Admin("Sarah", "Connor", "sconnor", "sarah@example.com", "Los Angeles")
admin_user.describe_user()
admin_user.show_privileges()