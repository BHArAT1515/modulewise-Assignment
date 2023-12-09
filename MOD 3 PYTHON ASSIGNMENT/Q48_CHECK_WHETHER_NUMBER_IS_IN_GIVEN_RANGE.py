def is_in_range(number, start, end):
    return start <= number <= end

# Example usage:
number_to_check = 15
start_range = 10
end_range = 20

if is_in_range(number_to_check, start_range, end_range):
    print(f"{number_to_check} is in the range between {start_range} and {end_range}.")
else:
    print(f"{number_to_check} is not in the specified range.")
