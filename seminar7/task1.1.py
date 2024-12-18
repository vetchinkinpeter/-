class Vector:
    def __init__(self, x, y, z):
        assert isinstance(x, (int, float))
        assert isinstance(y, (int, float))
        assert isinstance(z, (int, float))
        self.x = x
        self.y = y
        self.z = z
    def abs(self):
        return (self.x**2 + self.y**2 + self.z**2)**0.5

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        else:
            raise TypeError("можно складывать только два вектора")

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
        else:
            raise TypeError("можно вычитать только два вектора")

    def __mul__(self, other):
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y + self.z * other.z  # Dot product
        elif isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other, self.z * other)
        else:
            raise TypeError("можно умножать вектор на вектор или на число")

    def __str__(self):
        return f"{{ {self.x}, {self.y}, {self.z} }}"

    def __repr__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"
n = int(input())
sum = Vector(0,0,0)
for i in range(n):
    a = list(map(int, input().split()))
    a1 = Vector(a[0],a[1],a[2])
    sum = sum + a1
sum = sum * (1/n)
print(sum)

