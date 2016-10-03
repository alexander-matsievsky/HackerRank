import string

N = int(input())
letters = string.ascii_lowercase[:N]
fmt = '{:-^W}'.replace('W', str(4 * (len(letters) - 1) + 1))
print(sep='\n', *[fmt.format('-'.join(letters[N:abs(n):-1] + letters[abs(n):N])) for n in range(-N + 1, N)])
