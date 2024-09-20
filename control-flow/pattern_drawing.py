def draw_pattern():
    # Prompt user for pattern size
    size = int(input("Enter the size of the pattern: "))

    # Validate input
    if size <= 0:
        print("Please enter a positive integer.")
        return

    # Draw the pattern using nested loops
    row = 0
    while row < size:
        for col in range(size):
            print("*", end="")
        print()  # Move to the next line after each row
        row += 1

# Run the function to draw the pattern
if __name__ == "__main__":
    draw_pattern()