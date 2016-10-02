import sys

[_, numbers] = list(sys.stdin)
numbers = tuple(int(number) for number in numbers.split(' '))
print(hash(numbers))
