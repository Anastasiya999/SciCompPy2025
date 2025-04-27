from zestaw_6.zad_1 import Vector
import math
# Create a function find_axis(v1, v2) which returns the unit vector v3, where v3 is perpendicular to the vectors v1 and v2.
# If the vectors v1 and v2 are parallel (or zero) then the function should raise an exception (ValueError)
# [Hint: v1 and v2 are parallel if the cross product v1 × v2 is zero]. Vectors are instances of the Vector class from Homework 6.

def is_zero(v):
    return v.x == 0 and v.y == 0 and v.z == 0

def find_axis(a, b):
    is_zero_a = is_zero(a)
    is_zero_b = is_zero(b)
    if is_zero_a or is_zero_b:
        raise ValueError(f'{"first vector" if is_zero_a else "second vector"} is zero vector.')
    v3 = a.cross(b)
    if is_zero(v3):
        raise ValueError("v1 and v2 are parallel.")
    length = v3.length()
    return Vector(v3.x / length, v3.y / length, v3.z / length)

if __name__ == "__main__":

    v1 = Vector(1, 0, 0)
    v2 = Vector(0, 1, 0)

    v3 = find_axis(v1, v2)

    assert v3 == Vector(0.0, 0.0, 1.0)
    print("Non-parallel test passed.")

    v1 = Vector(0, 0, 0)
    v2 = Vector(1, 2, 3)

    try:
        find_axis(v1, v2)
    except ValueError as e:
        assert str(e) == "first vector is zero vector."
        print("Zero first vector test passed.")
    else:
        raise AssertionError("Expected ValueError for zero first vector.")

    v1 = Vector(1, 2, 3)
    v2 = Vector(0, 0, 0)

    try:
        find_axis(v1, v2)
    except ValueError as e:
        assert str(e) == "second vector is zero vector."
        print("Zero second vector test passed.")
    else:
        raise AssertionError("Expected ValueError for zero second vector.")

    v1 = Vector(1, 2, 3)
    v2 = Vector(2, 4, 6)

    try:
        find_axis(v1, v2)
    except ValueError as e:
        assert str(e) == "v1 and v2 are parallel."
        print("Parallel vectors test passed.")
    else:
        raise AssertionError("Expected ValueError for parallel vectors.")

    print("All tests passed.")



