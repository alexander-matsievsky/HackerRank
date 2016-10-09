from collections import Counter

occurrences = Counter(input().strip())
sorted_occurrences = sorted(occurrences.items(), key=lambda x: (-x[1], x[0]))
print(sep='\n', *['{} {}'.format(symbol, count) for symbol, count in sorted_occurrences[:3]])
