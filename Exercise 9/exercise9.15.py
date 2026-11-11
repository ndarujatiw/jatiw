from random import choice


def make_random_ticket(possibilities):
    """Generate a random 4-item lottery ticket."""
    ticket = []
    while len(ticket) < 4:
        item = choice(possibilities)
        if item not in ticket:
            ticket.append(item)
    return ticket


def check_ticket(played_ticket, winning_ticket):
    """Check if all items on the played ticket match the winning ticket."""
    for element in played_ticket:
        if element not in winning_ticket:
            return False
    return True


# Define possibilities and your specific ticket
possibilities = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "a", "b", "c", "d", "e"]
my_ticket = [7, 3, "a", 10]

loop_count = 0
won = False

print(f"Simulating lottery draws for your ticket: {my_ticket}...\n")

while not won:
    new_winning_ticket = make_random_ticket(possibilities)
    loop_count += 1
    if check_ticket(my_ticket, new_winning_ticket):
        won = True

print(f"Congratulations! Your ticket won after {loop_count:,} draws.")