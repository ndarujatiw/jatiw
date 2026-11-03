def make_shirt(size='large', message='Engineering'):
    """Summarize the size and message of a t-shirt."""
    print(f"Making a {size} t-shirt with the message: '{message}'.")

# Large shirt with default message
make_shirt()

# Medium shirt with default message
make_shirt(size='medium')

# Custom size and custom message
make_shirt('small', 'Salam Unity')