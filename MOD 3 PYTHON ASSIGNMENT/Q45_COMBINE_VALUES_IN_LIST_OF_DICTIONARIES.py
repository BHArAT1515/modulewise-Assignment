from collections import Counter

data_list = [
    {'item': 'item1', 'amount': 400},
    {'item': 'item2', 'amount': 300},
    {'item': 'item1', 'amount': 750}
]

combined_dict = Counter()

for item in data_list:
    combined_dict[item['item']] += item['amount']

print("Combined Dictionary:", combined_dict)
