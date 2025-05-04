# (a) Create a two dimensional array called m1, shape=(4,5).
# (b) Create a new array (or a view) m2 from m1, in which the elements of each row are in reverse order.
# (c) Create a new array (or a view) m3 from m1, in which the elements of each column are in reverse order.
# (d) Remove the first row, the last row, the first column, and the last column of m1, and create a new array (or a view) m4.

import numpy as np

if __name__ == "__main__":
    # (a)
    m1 = np.arange(1, 40, 2).reshape((4, 5)) # must be 4x5 len

    # (b)
    m2 = m1[:, ::-1]

    # (c)
    m3 = m1[::-1, :]

    # (d)
    m4 = m1[1:-1, 1:-1]

    # Results
    print("m1:\n", m1)
    print("m2 (rows reversed):\n", m2)
    print("m3 (columns reversed):\n", m3)
    print("m4 (without the first row, the last row, the first column, and the last column of m1):\n", m4)