def remove_duplicates(input_list):
    unique_list = list(set(input_list))
    return unique_list

# Example usage:
original_list = [1, 2, 2, 3, 4, 4, 5]
result_list = remove_duplicates(original_list)

print(f"Original List: {original_list}")
print(f"List with Duplicates Removed: {result_list}")
