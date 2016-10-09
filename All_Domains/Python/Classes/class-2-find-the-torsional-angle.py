from math import degrees, acos


class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross(self, other):
        return Vector(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** .5


A = Vector(*map(float, input().split()))
B = Vector(*map(float, input().split()))
C = Vector(*map(float, input().split()))
D = Vector(*map(float, input().split()))
X = (B - A).cross(C - B)
Y = (C - B).cross(D - C)
PHI = X.dot(Y) / abs(X) / abs(Y)
print(round(degrees(acos(PHI)), 2))
