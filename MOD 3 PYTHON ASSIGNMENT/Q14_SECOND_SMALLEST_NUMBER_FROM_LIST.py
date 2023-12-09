def second_smallest_number(input_list):
    sorted_list = sorted(set(input_list))
    return sorted_list[1] if len(sorted_list) > 1 else None

# Example usage:
numbers = [5, 2, 8, 1, 7, 3]
result = second_smallest_number(numbers)
print("Original List:", numbers)
print("Second Smallest Number:", result)
