print("Welcome to the Addition Calculator!")
print("Enter 'q' at any time to quit.\n")

while True:
    first_number = input("\nFirst number: ")
    if first_number.lower() == "q":
        break
        
    second_number = input("Second number: ")
    if second_number.lower() == "q":
        break

    try:
        answer = int(first_number) + int(second_number)
    except ValueError:
        print("Oops! Invalid input. Please enter numbers only.")
    else:
        print(f"The sum is: {answer}")