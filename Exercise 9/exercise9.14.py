from random import choice

# Create a list containing 10 numbers and 5 letters
possibilities = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "a", "b", "c", "d", "e"]

winning_ticket = []
print("Let's select a winning lottery combination...")

# Pull 4 random items without duplicates
while len(winning_ticket) < 4:
    pulled_item = choice(possibilities)
    if pulled_item not in winning_ticket:
        winning_ticket.append(pulled_item)

print(
    f"Any ticket matching these 4 numbers or letters wins a prize: {winning_ticket}"
)