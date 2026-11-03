def make_shirt(size, message):
    """Summarize the size and message of a t-shirt."""
    print(f"Making a {size} t-shirt with the message: '{message}'.")

# Call with positional arguments
make_shirt('medium', 'Indus Hebat')

# Call with keyword arguments
make_shirt(message='Indus Kuat', size='small')