filenames = ["cats.txt", "dogs.txt", "birds.txt"]  # 'birds.txt' doesn't exist

for filename in filenames:
    try:
        with open(filename) as f:
            contents = f.read()
            print(f"\n--- {filename} ---")
            print(contents.strip())
    except FileNotFoundError:
        pass  # Fails silently without crashing or printing an error message