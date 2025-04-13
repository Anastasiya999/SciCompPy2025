import math

class Vector:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f'Vector({self.x}, {self.y}, {self.z})'

    def __eq__(self, other):   # v == w
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __ne__(self, other):        # v != w
        return not self == other

    def __add__(self, other):  # v + w
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):   # v - w
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):  # return the dot product (number)
        return self.x * other.x + self.y * other.y + self.z * other.z

    def __neg__(self):  # -v
        return Vector(-self.x, -self.y, -self.z)

    def cross(self, other):   # return the cross product (Vector)
        x = self.y * other.z - self.z * other.y
        y = self.x * other.z - self.z * other.x
        z = self.x * other.y - self.y * other.x
        return Vector(x, -y, z)

    def length(self):    # the length of the vector
        return math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)

    def __hash__(self):   # we assume that vectors are immutable
        return hash((self.x, self.y, self.z))   # recommended


if __name__ == "__main__":
    # Exemplary tests. Change values in your tests.
    v = Vector(1, 2, 3)
    w = Vector(2, -3, 2)

    assert v != w
    assert v + w == Vector(3, -1, 5)
    assert v - w == Vector(-1, 5, 1)
    assert v * w == 2
    assert v.cross(w) == Vector(13, 4, -7)
    assert v.length() == math.sqrt(14)
    S = set([v, v, w])
    assert len(S) == 2

    print("Tests passed")

    # Additional tests

    # String representation
    assert repr(Vector(3, 4, 5)) == "Vector(3, 4, 5)"

    # Equality
    assert Vector(0, 0, 0) == Vector(0, 0, 0)
    assert Vector(-1, -2, -3) == Vector(-1, -2, -3)

    # Inequality
    assert Vector(1, 0, 0) != Vector(0, 1, 0)

    # Addition
    v1 = Vector(4, 5, 6)
    v2 = Vector(-1, 2, -3)
    assert v1 + v2 == v2 + v1

    # Subtraction
    assert v1 - v2 == -(v2 - v1)

    # Dot product commutativity
    assert v1 * v2 == v2 * v1

    # Cross product
    assert v1.cross(v2) == Vector(
        v1.y * v2.z - v1.z * v2.y,
        -(v1.x * v2.z - v1.z * v2.x),
        v1.x * v2.y - v1.y * v2.x,
    )
    assert v1.cross(v2) == -v2.cross(v1)

    # Length of a unit vector
    unit = Vector(1 / math.sqrt(3), 1 / math.sqrt(3), 1 / math.sqrt(3))
    assert math.isclose(unit.length(), 1.0)

    # Dot product with zero vector
    zero = Vector(0, 0, 0)
    assert v * zero == 0
    assert v.cross(zero) == zero
    assert zero.length() == 0

    print("All additional tests passed")

