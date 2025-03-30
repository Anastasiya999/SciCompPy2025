# Create the following infinite generators:
# (a) iter_even(), producing even numbers (0, 2, 4, ...),
# (b) iter_odd(), producing odd numbers (1, 3, 5, ...),
# (c) iter_power(k), producing powers of k (1, k, k*k, k*k*k, ...).

# (a)
def iter_even():
    n = 0
    while True:
        yield n
        n += 2

# (b)
def iter_odd():
    n = 1
    while True:
        yield n
        n += 2

# (c)
def iter_power(k):
    n = 1
    while True:
        yield n
        n *= k

# Sample outputs
odd_generator = iter_odd()
print(next(odd_generator), next(odd_generator), next(odd_generator))

even_generator = iter_even()
print(next(even_generator), next(even_generator), next(even_generator))

power_generator = iter_power(3)
print(next(power_generator), next(power_generator), next(power_generator))