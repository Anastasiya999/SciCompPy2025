# Reversing a part of a list in place, reverse_range(L, left, right), the right index is included.
# Write iterative and recursive versions.

# # Example.
# L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# reverse_range(L, 3, 6)   # index 6 is included!
# print(L)   # [0, 1, 2, 6, 5, 4, 3, 7, 8, 9]   # the list L changed
# # The numbers outside the range are intact.

# Assumtion: left <= right

def reverse_range_iterative(L, left, right):
    left_idx = max(0, left)
    right_idx = min(len(L) - 1, right)
    while left_idx < right_idx:
        temp = L[left_idx]
        L[left_idx] = L[right_idx]
        L[right_idx] = temp
        right_idx -= 1
        left_idx += 1

def reverse_range_recursive(L, left, right):
    left_idx = max(0, left)
    right_idx = min(len(L) - 1, right)
    if left_idx < right_idx:
        temp = L[left_idx]
        L[left_idx] = L[right_idx]
        L[right_idx] = temp
        reverse_range_recursive(L, left_idx + 1, right_idx - 1)

L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
L_copy = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
reverse_range_iterative(L, 3, 6)
reverse_range_recursive(L_copy,3, 6)
print(L, L_copy)

