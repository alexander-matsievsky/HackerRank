import cmath

z = complex(input())
print(sep='\n', *[abs(z), cmath.phase(z)])
