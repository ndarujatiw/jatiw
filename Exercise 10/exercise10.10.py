def analyze_word_count(filename, target_word):
    """Count approximate occurrences of a word in a text file."""
    try:
        with open(filename, encoding="utf-8") as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} could not be found.")
    else:
        # Convert to lowercase to catch uppercase variants at the start of sentences
        count = contents.lower().count(target_word)
        print(f"The search term '{target_word}' appears about {count:,} times in {filename}.")


# Example usage (assuming you have a text file like 'alice.txt')
filename = "alice.txt"

print(f"Analyzing {filename}...")
analyze_word_count(filename, "the")
analyze_word_count(filename, "the ")