import json

filename = "user_profile.json"


def get_stored_user_data(filename):
    """Get stored user data if it exists."""
    try:
        with open(filename) as f:
            user_data = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return user_data


def get_new_user_data(filename):
    """Prompt user for multiple pieces of information and save them."""
    user_data = {}
    user_data["username"] = input("What is your username? ")
    user_data["age"] = input("How old are you? ")
    user_data["favorite_language"] = input("What is your favorite programming language? ")

    with open(filename, "w") as f:
        json.dump(user_data, f)
    return user_data


def display_user_profile():
    """Display a summary of stored user information."""
    user_data = get_stored_user_data(filename)

    if user_data:
        print(f"\nWelcome back, {user_data['username']}! Here is what I remember about you:")
        print(f"- Username: {user_data['username']}")
        print(f"- Age: {user_data['age']}")
        print(f"- Favorite Programming Language: {user_data['favorite_language']}")
    else:
        user_data = get_new_user_data(filename)
        print(f"\nWe've saved your profile and will remember you next time, {user_data['username']}!")


display_user_profile()