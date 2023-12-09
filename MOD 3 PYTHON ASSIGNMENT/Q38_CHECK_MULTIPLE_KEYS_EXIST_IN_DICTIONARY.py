my_dict = {'one': 1, 'two': 2, 'three': 3}

keys_to_check = ['two', 'four', 'five']

for key in keys_to_check:
    if key in my_dict:
        print(f"The key '{key}' exists in the dictionary with value {my_dict[key]}.")
    else:
        print(f"The key '{key}' does not exist in the dictionary.")
