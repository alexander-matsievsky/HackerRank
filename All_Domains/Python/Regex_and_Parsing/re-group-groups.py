import re

S = input().strip()
s = re.search(r'([^\W_])\1+', S)
print(s.group(1) if s else -1)
