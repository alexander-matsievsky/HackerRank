import sys

[_, numbers, *_] = list(sys.stdin)
numbers = tuple(int(number) for number in numbers.split(' '))
print(hash(numbers))
