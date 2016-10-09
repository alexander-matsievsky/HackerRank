import re

T = int(input())
for _ in range(0, T):
    try:
        re.compile(input().strip())
        print(True)
    except re.error:
        print(False)
