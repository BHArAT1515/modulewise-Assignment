def is_list_empty(input_list):
    return not bool(input_list)

# Example usage:
empty_list = []
non_empty_list = [1, 2, 3]

if is_list_empty(empty_list):
    print("The list is empty.")
else:
    print("The list is not empty.")

if is_list_empty(non_empty_list):
    print("The list is empty.")
else:
    print("The list is not empty.")
