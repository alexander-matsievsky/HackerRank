import re
import sys

[NM, *rows] = list(sys.stdin)
[N, M] = list(map(int, NM.split()))
script = ''.join(rows[n][m] for m in range(0, M) for n in range(0, N))
print(re.sub(r'(?<=[^\W_])([^\w])+(?=[^\W_])', ' ', script))
