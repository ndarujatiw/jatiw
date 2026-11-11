import json


def get_stored_username(filename):
    """Get stored username if available."""
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username(filename):
    """Prompt for a new username and store it."""
    username = input("What is your name? ")
    with open(filename, "w") as f:
        json.dump(username, f)
    return username


def greet_user():
    """Greet the user by name, verifying if the current user is correct."""
    filename = "username.json"
    username = get_stored_username(filename)

    if username:
        correct = input(f"Are you {username}? (y/n): ")
        if correct.lower() == "y":
            print(f"Welcome back, {username}!")
            return

    # If file doesn't exist or the user answered 'n'
    username = get_new_username(filename)
    print(f"We'll remember you when you come back, {username}!")


greet_user()