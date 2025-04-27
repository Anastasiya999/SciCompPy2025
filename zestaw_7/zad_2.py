import itertools
import random

# Create the following infinite iterators:
# (a) returning 0, 1, 0, 1, 0, 1, ...,
# (b) returning randomly 0 or 1 on demand,
# (c) returning 0, 1, 0, -1, 0, 1, 0, -1, ...

# a
def zero_one_inf_iterator():
    while True:
        yield 0
        yield 1



# b
def random_zero_one_inf_iterator():
    while True:
        yield random.choice([0, 1])


# c
def zero_one_zero_minus_one_iterator():
    return itertools.cycle([0, 1, 0, -1])

def test_zero_one_inf_iterator():
    it = zero_one_inf_iterator()

    result = [next(it) for _ in range(6)]

    assert result == [0, 1, 0, 1, 0, 1]


def test_random_zero_one_inf_iterator():
    it = random_zero_one_inf_iterator()

    result = [next(it) for _ in range(10)]

    for value in result:
        assert value in (0, 1)


def test_zero_one_zero_minus_one_iterator():
    it = zero_one_zero_minus_one_iterator()

    result = [next(it) for _ in range(8)]

    assert result == [0, 1, 0, -1, 0, 1, 0, -1]


if __name__ == "__main__":
    test_zero_one_inf_iterator()
    test_random_zero_one_inf_iterator()
    test_zero_one_zero_minus_one_iterator()
    print("All tests passed")