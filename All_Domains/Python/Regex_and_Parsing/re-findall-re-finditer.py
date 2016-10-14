import re

S = input().strip()
vowels = re.findall(r'(?<={consonant})({vowels})(?={consonant})'.format(
    consonant='[qwrtypsdfghjklzxcvbnm]',
    vowels='[aeiou]{2,}'
), S, re.IGNORECASE)
print(sep='\n', *(vowels or [-1]))
