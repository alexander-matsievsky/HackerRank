import sys

[_, s, _, *commands] = list(sys.stdin)
s = set(int(x) for x in s.strip().split(' '))
commands = [command.strip().split(' ') for command in commands]
for [command, *args] in commands:
    args = list(map(int, args))
    {
        'pop': lambda: len(s) > 0 and s.pop(),
        'remove': lambda: args[0] in s and s.remove(args[0]),
        'discard': lambda: s.discard(args[0])
    }.get(command, lambda: None)()

print(sum(s))
