# Find the sum 1*1 + 3*3 + 5*5 + ... + 2021*2021 [hint: use sum() and range()].

def find_squared_sum_up_to(max_value):
    return sum([x * x for x in range(1, max_value + 1)])

print(find_squared_sum_up_to(2021))