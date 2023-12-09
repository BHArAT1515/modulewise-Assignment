import itertools

data = {'1': ['a', 'b'], '2': ['c', 'd']}

combinations = [''.join(comb) for comb in itertools.product(*data.values())]
print("All Combinations of Letters:", ' '.join(combinations))
