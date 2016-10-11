import re
import sys

test_cases = [line.strip() for line in list(sys.stdin)[1:]]
float_regex = re.compile(r'''
# Number can start with +, - or . symbol.
# Number must contain at least 1 decimal value.
# Number must have exactly one `.` symbol.
^
[+-]?
\d*
\.
\d+
$
''', re.VERBOSE)
print(sep='\n', *[bool(float_regex.match(test_case)) for test_case in test_cases])
