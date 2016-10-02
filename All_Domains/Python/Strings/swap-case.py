import string
import sys


def switch_case(letter):
    if letter in string.ascii_lowercase:
        return letter.upper()
    if letter in string.ascii_uppercase:
        return letter.lower()
    return letter


print(''.join(map(switch_case, sys.stdin.read())))
