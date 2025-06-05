from itertools import groupby
s = input()
grouped_numbers = groupby(s, key=lambda x: x)
result = ' '.join(f"({len(list(group))}, {key})" for key, group in grouped_numbers)
print(result)
