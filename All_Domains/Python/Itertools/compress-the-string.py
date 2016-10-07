import itertools

S = input().strip()
print(sep=' ', *[(len(list(g)), int(s)) for s, g in itertools.groupby(S)])
