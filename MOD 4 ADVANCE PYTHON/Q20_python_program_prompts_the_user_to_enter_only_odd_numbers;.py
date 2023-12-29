try:
    user_input = int(input("Enter an odd number: "))
    if user_input % 2 == 0:
        raise ValueError("Even number entered. Please enter an odd number.")
except ValueError as ve:
    print(f"Error: {ve}")
