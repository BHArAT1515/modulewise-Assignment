def contains_sublist(main_list, sublist):
    return all(item in main_list for item in sublist)

# Example usage:
main_list = [1, 2, 3, 4, 5]
sub_list = [3, 4]
result = contains_sublist(main_list, sub_list)
print("Main List:", main_list)
print("Sub List:", sub_list)
print("Contains Sub List:", result)
