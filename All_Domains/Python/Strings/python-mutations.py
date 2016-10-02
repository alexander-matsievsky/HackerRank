import sys

[string, replacement] = list(sys.stdin)
[index, symbol] = replacement.split(' ')
index = int(index)

print(string[:index] + symbol + string[index + 1:])
