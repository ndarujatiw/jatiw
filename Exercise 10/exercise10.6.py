print("Enter two numbers to add them together.")

first_number = input("First number: ")
second_number = input("Second number: ")

try:
    x = int(first_number)
    y = int(second_number)
except ValueError:
    print(
        "Friendly error: Please make sure you enter numbers only, not text!"
    )
else:
    answer = x + y
    print(f"The sum of {x} and {y} is {answer}.")