def unzip_tuples(tuple_list):
    return list(zip(*tuple_list))

# Example usage:
original_list = [(1, 'one'), (2, 'two'), (3, 'three')]
result = unzip_tuples(original_list)
print("Original List of Tuples:", original_list)
print("Unzipped Lists:", result)
