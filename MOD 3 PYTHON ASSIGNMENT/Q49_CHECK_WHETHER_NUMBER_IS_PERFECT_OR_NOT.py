def is_perfect_number(number):
    divisors = [i for i in range(1, number) if number % i == 0]
    return sum(divisors) == number

# Example usage:
number_to_check = 28

if is_perfect_number(number_to_check):
    print(f"{number_to_check} is a perfect number.")
else:
    print(f"{number_to_check} is not a perfect number.")
