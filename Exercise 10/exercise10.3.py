filename = "learning_python.txt"

print("--- Using splitlines() directly in the loop ---")
with open(filename) as file_object:
    contents = file_object.read()

# Loop directly over the list returned by splitlines() without a temporary variable
for line in contents.splitlines():
    print(line)