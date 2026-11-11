#store_number.py
import json

favorite_number = input("What is your favorite number? ")
filename = "favorite_number.json"

# Use json.dumps() to serialize or json.dump() to write directly to file
with open(filename, "w") as f:
    json.dump(favorite_number, f)

print(f"Thanks! I've saved your favorite number.")

#read_number.py
import json

filename = "favorite_number.json"

try:
    with open(filename) as f:
        favorite_number = json.load(f)
except FileNotFoundError:
    print("I don't know your favorite number yet.")
else:
    print(f"I know your favorite number! It’s {favorite_number}.")