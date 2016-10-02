import sys

[_, numbers] = list(sys.stdin)
numbers = [int(number) for number in numbers.split(' ')]
unique = list(set(numbers))
print(sorted(unique)[-2])
