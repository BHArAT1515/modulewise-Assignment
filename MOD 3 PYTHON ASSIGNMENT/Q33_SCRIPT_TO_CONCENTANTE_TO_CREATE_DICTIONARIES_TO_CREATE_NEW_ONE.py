dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
dict3 = {'e': 5}

# Concatenate dictionaries
new_dict = {**dict1, **dict2, **dict3}

print("Dictionary 1:", dict1)
print("Dictionary 2:", dict2)
print("Dictionary 3:", dict3)
print("Concatenated Dictionary:", new_dict)
