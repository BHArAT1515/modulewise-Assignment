def have_common_member(list1, list2):
    set1 = set(list1)
    set2 = set(list2)

    common_elements = set1.intersection(set2)

    return bool(common_elements)

list_a = [1, 2, 3, 4, 5]
list_b = [5, 6, 7, 8, 9]

if have_common_member(list_a, list_b):
    print("The lists have at least one common member.")
else:
    print("The lists do not have any common members.")
