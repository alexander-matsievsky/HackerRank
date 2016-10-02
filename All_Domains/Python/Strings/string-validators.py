import sys

[string] = list(sys.stdin)
print(any(letter.isalnum() for letter in string))
print(any(letter.isalpha() for letter in string))
print(any(letter.isdigit() for letter in string))
print(any(letter.islower() for letter in string))
print(any(letter.isupper() for letter in string))
