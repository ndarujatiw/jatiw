filenames = ["cats.txt", "dogs.txt"]

for filename in filenames:
    print(f"\n--- Attempting to read: {filename} ---")
    try:
        with open(filename) as f:
            contents = f.read()
            print(contents.strip())
    except FileNotFoundError:
        print(f"Sorry, we couldn't find the file '{filename}'.")