filename = "guest.txt"

# Prompt the user for their name
name = input("Please enter your name: ")

# Open the file in write mode ('w') and write the name
with open(filename, "w") as file_object:
    file_object.write(name)

print(f"Thank you, {name}. Your name has been saved to {filename}.")