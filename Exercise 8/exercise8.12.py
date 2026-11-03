def make_sandwich(*items):
    """Print a summary of the sandwich being ordered."""
    print("\nMaking a sandwich with the following items:")
    for item in items:
        print(f"- {item}")

make_sandwich('roast beef', 'cheddar cheese', 'lettuce', 'honey mustard')
make_sandwich('turkey', 'apple slices')
make_sandwich('peanut butter', 'strawberry jam')