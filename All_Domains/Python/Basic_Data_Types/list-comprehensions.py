import sys

[X, Y, Z, N] = [int(line) for line in sys.stdin]
print([[x, y, z]
       for x in range(0, X + 1)
       for y in range(0, Y + 1)
       for z in range(0, Z + 1)
       if not x + y + z == N])
