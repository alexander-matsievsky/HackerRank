import re

[S, k] = [input().strip(), input().strip()]
print(sep='\n', *(
    [(s.start(), s.start() + len(k) - 1) for s in re.finditer(r'(?=({}))'.format(k), S)] or [(-1, -1)]
))
