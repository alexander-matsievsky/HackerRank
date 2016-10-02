import sys

list = []
for line in sys.stdin:
    [command, *args] = line.split(' ')
    command = command.strip()
    args = [int(arg) for arg in args]
    {
        'insert': lambda: list.insert(args[0], args[1]),
        'print': lambda: print(list),
        'remove': lambda: list.remove(args[0]),
        'append': lambda: list.append(args[0]),
        'sort': lambda: list.sort(),
        'pop': lambda: list.pop(),
        'reverse': lambda: list.reverse(),
    }.get(command, lambda: None)()
