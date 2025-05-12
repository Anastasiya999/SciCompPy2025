# Generate n=100 random points in a unit square [0,1]x[0,1].
# Points are green if the distance from (0,0) is less then 1; they are red otherwise.
# The marker area of a point (x,y) should be proportional to |x|+|y|.


import numpy as np
import matplotlib.pyplot as plt


def scatter_points_by_radius(n=100, color_inside='green', color_outside='red', scale=500, figsize=6,):
    threshold = 1
    x = np.random.rand(n)
    y = np.random.rand(n)


    distance = np.sqrt(x ** 2 + y ** 2)
    sizes = (np.abs(x) + np.abs(y)) * scale

    plt.figure(figsize=(figsize, figsize))

    inside_points = plt.scatter(x[distance < threshold], y[distance < threshold],
                                c=color_inside, s=sizes[distance < threshold],
                                alpha=0.6,  label=f'Inside circle (< 1)')

    outside_points = plt.scatter(x[distance >= threshold], y[distance >= threshold],
                                 c=color_outside, s=sizes[distance >= threshold],
                                 alpha=0.6,  label=f'Outside circle (≥ 1)')

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(f'{n} Random Points in [0,1] x [0,1]')
    plt.grid(True)
    plt.axis('equal')
    plt.tight_layout()


    plt.legend(handles=[inside_points, outside_points])

    plt.show()

if __name__ == "__main__":

    scatter_points_by_radius()