from random import randint


class Die:
    """A class representing a single die."""

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        """Return a random number between 1 and the number of sides."""
        return randint(1, self.sides)


# 1. Make a 6-sided die and roll it 10 times
d6 = Die()
print("Rolling a 6-sided die 10 times:")
results_6 = [d6.roll_die() for _ in range(10)]
print(results_6)

# 2. Make a 10-sided die and roll it 10 times
d10 = Die(10)
print("\nRolling a 10-sided die 10 times:")
results_10 = [d10.roll_die() for _ in range(10)]
print(results_10)

# 3. Make a 20-sided die and roll it 10 times
d20 = Die(20)
print("\nRolling a 20-sided die 10 times:")
results_20 = [d20.roll_die() for _ in range(10)]
print(results_20)