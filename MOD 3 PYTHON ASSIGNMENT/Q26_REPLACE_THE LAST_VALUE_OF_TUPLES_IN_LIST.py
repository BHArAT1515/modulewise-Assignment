def replace_last_value(tuples_list, new_value):
    modified_list = [t[:-1] + (new_value,) for t in tuples_list]
    return modified_list

# Example usage:
original_list = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
new_value = 10
result_list = replace_last_value(original_list, new_value)
print("Original List:", original_list)
print("List with Last Value Replaced:", result_list)
