filename = "guest_book.txt"

print("Enter 'quit' at any time to exit the guest book program.\n")

# Open the file in write mode ('w') outside or append mode ('a') depending on preference; 
# using 'w' overwrites previous runs, while 'a' adds to it. Let's use 'a' so multiple runs accumulate names.
with open(filename, "a") as file_object:
    while True:
        name = input("Please enter your name: ")
        
        if name.lower() == "quit":
            print("\nExiting the guest book. Have a great day!")
            break
        
        # Write the name followed by a newline character
        file_object.write(f"{name}\n")
        print(f"Welcome, {name}! Your name has been added to the guest book.")