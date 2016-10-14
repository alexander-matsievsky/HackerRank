import re
import sys

lines = list(sys.stdin)[1:]
print(sep='', *[re.sub(r'(?<= )&&(?= )', 'and', re.sub(r'(?<= )\|\|(?= )', 'or', line)) for line in lines])
