def find_repeated_items(my_tuple):
    repeated_items = set(item for item in my_tuple if my_tuple.count(item) > 1)
    return list(repeated_items)

# Example usage:
my_tuple = (1, 2, 2, 3, 4, 4, 5)
result = find_repeated_items(my_tuple)
print("Original Tuple:", my_tuple)
print("Repeated Items:", result)
