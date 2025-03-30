# Find and explain the results.
t = (2, 4)
print(t[2])
t.append(6)
a, b = t ; print(a, b)

#-------Explanation--------
# There is an error, when trying to execute t[2]: IndexError: tuple index out of range
# Cause: we index elements from 0, so in tuple with two elements the max index is 1

# There is an error, when trying to execute t.append(6)
# Cause: we cannot append, as tuples are immutable and there is no such method append
