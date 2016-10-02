import sys

[first_name, last_name] = [line.strip() for line in sys.stdin]

print('Hello {} {}! You just delved into python.'.format(first_name, last_name))
