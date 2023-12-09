def remove_empty_tuples(tuple_list):
    non_empty_tuples = [t for t in tuple_list if t]
    return non_empty_tuples

# Example usage:
original_list = [(1, 2), (), (3, 4), (), (5, 6)]
result_list = remove_empty_tuples(original_list)
print("Original List:", original_list)
print("List with Empty Tuples Removed:", result_list)
