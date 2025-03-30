# Let p=(x,y) be a point in a plane. Define the following functions using lambda:
# (a) a test if p is in unit (filled) circle,
# (b) a test if the coordinates of p are positive,
# (c) a sorting key (y decreasing, x increasing),
# (d) a sorting key (the sum |x|+|y|).

is_in_unit_circle = lambda p: p[0]**2 + p[1]**2 <= 1

has_positive_coordinates = lambda p: p[0] > 0 and p[1] > 0

sort_by_yDesc_xAsc = lambda p:  (p[0], -p[1])

sort_by_abs_sum = lambda p: abs(p[0]) + abs(p[1])

# sample inputs
points = [(2, 3), (-2, -3),  (0.5, 0.5), (1, 1.5)]

filtered_points = list(filter(is_in_unit_circle, points))

sorted_yx = sorted(points, key=sort_by_yDesc_xAsc)

sorted_abs_sum = sorted(points, key=sort_by_abs_sum)

print(f"Points: {points}")
print(f"Filtered points: {filtered_points}")
print(f"Sorted (a sorting key (x increasing, y decreasing)): {sorted_yx}")
print(f"Sorted (a sorting key (the sum |x|+|y|)): {sorted_abs_sum}")
