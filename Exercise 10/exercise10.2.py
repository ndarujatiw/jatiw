filename = "learning_python.txt"

print("--- Translating Python learning points to C ---")
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    # Replace 'Python' with 'C' and strip trailing whitespace/newlines
    modified_line = line.replace("Python", "C")
    print(modified_line.strip())