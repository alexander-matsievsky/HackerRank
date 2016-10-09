class Complex:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def __add__(self, other):
        return Complex(self.i + other.i, self.j + other.j)

    def __sub__(self, other):
        return Complex(self.i - other.i, self.j - other.j)

    def __mul__(self, other):
        return Complex(
            self.i * other.i - self.j * other.j,
            self.i * other.j + self.j * other.i
        )

    def __truediv__(self, other):
        return Complex(
            (self.i * other.i + self.j * other.j) / (other.i ** 2 + other.j ** 2),
            (self.j * other.i - self.i * other.j) / (other.i ** 2 + other.j ** 2)
        )

    def __abs__(self):
        return Complex((self.i ** 2 + self.j ** 2) ** .5, 0)

    def __repr__(self):
        return '{:.2f}{:+.2f}i'.format(self.i, self.j)


[C, D] = [Complex(*map(float, input().split())), Complex(*map(float, input().split()))]
print(sep='\n', *(C + D, C - D, C * D, C / D, abs(C), abs(D)))
