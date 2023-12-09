def get_list_stats(numbers):
    if not numbers:
        return None, None, 0  # If the list is empty, return None for both largest and smallest, and 0 for sum

    largest = max(numbers)
    smallest = min(numbers)
    total_sum = sum(numbers)

    return largest, smallest, total_sum

list_of_sum = [5, 10, 2, 8, 15]
largest_num, smallest_num, sum_of_all = get_list_stats(list_of_sum)

print(f"Largest number: {largest_num}")
print(f"Smallest number: {smallest_num}")
print(f"Sum of all numbers: {sum_of_all}")
