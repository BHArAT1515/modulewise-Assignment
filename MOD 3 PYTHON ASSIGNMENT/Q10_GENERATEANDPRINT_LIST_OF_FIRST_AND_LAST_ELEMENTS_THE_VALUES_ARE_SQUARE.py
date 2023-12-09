def generate_square_list():
    # Generate a list of squares of numbers between 1 and 30
    square_list = [i**2 for i in range(1, 31)]
    return square_list

squares = generate_square_list()

# Print the first 5 elements
print("First 5 elements:", squares[:5])

# Print the last 5 elements
print("Last 5 elements:", squares[-5:])
