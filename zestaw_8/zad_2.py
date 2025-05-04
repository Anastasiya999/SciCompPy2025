# (a) Create an arbitrary one dimensional array called v1.
# (b) Create a new array (or a view) v2 which consists of items with odd indices of v1.
# (c) Create a new array (or a view) v3 in backwards ordering from v1.
import numpy as np

if __name__ == "__main__":
    # (a)
    v1 = np.array([ 1, 2, 3, 5, 8, 13, 21])

    # (b)
    v2 = v1[1::2]
    # alternatives:
    # v2 = v1[np.arange(1, len(v1), 2)]
    # v2 = v1[np.where(np.arange(len(v1)) % 2 == 1)]
    # v2 = np.array([v1[i] for i in range(len(v1)) if i % 2 == 1])

    # (c)
    v3 = v1[::-1]

    # Results
    print("an arbitrary one dimensional array v1:\n", v1)
    print("a new view v2 which consists of items with odd indices of v1:\n", v2)
    print("a new view v3 in backwards ordering from v1:\n", v3)