def find_max_min(*numbers):
    if not numbers:
        return None, None
    
    max_number = max(numbers)
    min_number = min(numbers)
    
    return max_number, min_number

# Example usage:
decimal_numbers = (3.14, 1.23, 5.67, 2.34, 4.56)
max_value, min_value = find_max_min(*decimal_numbers)
print(f"Maximum number: {max_value}")
print(f"Minimum number: {min_value}")
