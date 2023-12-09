my_dict = {'one': 1, 'three': 3, 'five': 5, 'two': 2, 'four': 4}

# Sort in ascending order by value
ascending_sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))

# Sort in descending order by value
descending_sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))

print("Original Dictionary:", my_dict)
print("Ascending Sorted Dictionary:", ascending_sorted_dict)
print("Descending Sorted Dictionary:", descending_sorted_dict)
