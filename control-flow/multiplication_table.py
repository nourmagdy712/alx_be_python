def multiplication_table():
    # Prompt user for a number
    number = int(input("Enter a number to see its multiplication table: "))

    # Generate and print the multiplication table
    print(f"Multiplication Table for {number}:")
    for i in range(1, 11):
        product = number * i
        print(f"{number} * {i} = {product}")

# Run the function to display the multiplication table
if __name__ == "__main__":
    multiplication_table()