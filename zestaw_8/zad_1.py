import numpy as np

# Create the following NumPy arrays:
# (a) float from 0.0 to 1.0 step 0.1, shape=(11,),
# (b) int zeros (1 byte) with shape=(5,6),
# (c) complex with shape=(9,), powers of x = complex(0, 1): 1, x, x**2, ..., x**8.


# (a)
def create_float_array(start=0.0, end=1.0, step=0.1):
    return np.arange(start, end + step, step, dtype=float)

# (b)
def create_zero_int_array(shape=(5, 6)):
    return np.zeros(shape, dtype=np.int8)

# (c)
def create_complex_powers(base=complex(0, 1), count=9):
    return np.array([base**n for n in range(count)], dtype=complex)


if __name__ == "__main__":
    # Usage
    a = create_float_array()
    b = create_zero_int_array()
    c = create_complex_powers()

    # Results
    print("float from 0.0 to 1.0 step 0.1, shape=(11,): ", a)
    print("int zeros (1 byte) with shape=(5,6): ", b)
    print("complex with shape=(9,), powers of x = complex(0, 1): ", c)
