def send_messages(messages, sent_messages):
    """Print each message and move it to the sent_messages list."""
    while messages:
        current_message = messages.pop(0)
        print(f"Sending message: {current_message}")
        sent_messages.append(current_message)

short_messages = ["running late", "see you at 5", "don't forget the milk"]
sent_messages = []

send_messages(short_messages, sent_messages)

print(f"\nOriginal list: {short_messages}")
print(f"Sent messages: {sent_messages}")