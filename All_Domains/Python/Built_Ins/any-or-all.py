[_, ns] = [input(), input().split()]
print(all(int(n) >= 0 for n in ns) and any(n == ''.join(reversed(n)) for n in ns))
