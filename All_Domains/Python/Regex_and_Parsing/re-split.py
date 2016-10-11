import re

print(sep='\n', *[s for s in re.split(r'''[.,]''', input().strip()) if re.match(r'''\d+''', s)])
