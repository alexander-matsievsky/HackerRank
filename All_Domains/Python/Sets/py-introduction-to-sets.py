import sys

[N, heights] = list(sys.stdin)
N = int(N)
heights = set(float(height) for height in heights.split(' '))
print(sum(heights) / len(heights))
