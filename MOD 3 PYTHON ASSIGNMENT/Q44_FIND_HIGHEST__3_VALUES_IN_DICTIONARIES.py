my_dict = {'a': 100, 'b': 500, 'c': 300, 'd': 200, 'e': 400}

sorted_items = sorted(my_dict.items(), key=lambda x: x[1], reverse=True)
highest_3_values = dict(sorted_items[:3])

print("Original Dictionary:", my_dict)
print("Highest 3 Values in the Dictionary:", highest_3_values)
