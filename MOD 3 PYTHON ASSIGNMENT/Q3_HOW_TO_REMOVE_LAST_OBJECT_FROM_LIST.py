
def remove_last_element(my_list):
    if my_list:  
        my_list.pop()
    else:
        print("The list is empty.")

list1 = [2, 33, 222, 14, 25]

remove_last_element(list1)

print("Modified list:", list1)