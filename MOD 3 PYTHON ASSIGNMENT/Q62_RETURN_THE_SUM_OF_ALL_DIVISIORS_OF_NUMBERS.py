def sum_of_divisors(number):
    divisors = [i for i in range(1, number + 1) if number % i == 0]
    return sum(divisors)

# Example usage:
number_to_check = 12
divisor_sum = sum_of_divisors(number_to_check)
print(f"The sum of divisors of {number_to_check} is: {divisor_sum}")
