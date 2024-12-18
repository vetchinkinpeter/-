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
v1 = Vector(1, 2, 3)
v2 = Vector(4,5,6)
v3 = Vector(1, 2, 3)

print(f"v1: {v1}")
print(f"v2: {v2}")
print(f"v1 + v2: {v1 + v2}")
print(f"v1 - v2: {v1 - v2}")
print(f"scalar v1*v2: {v1 * v2}")
print(f"vector v1*2: {v1 * 2}")
print(f"|v1|: {v1.abs()}")
