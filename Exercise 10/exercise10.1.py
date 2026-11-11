filename = "C:/Users/user/Documents/Prokom/alproa/Exercise/learning_python.txt"

# 1. Read in the entire file at once
print("--- Reading in the entire file ---")
with open(filename) as file_object:
    contents = file_object.read()
print(contents)

# 2. Store lines in a list and loop over each line
print("--- Storing lines in a list and looping ---")
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.strip())  # .strip() removes extra blank lines caused by newlines