# Create a long positive integer.
# Find the number of zeros. Hint: change the number to a string.

def calculate_number_of_zeros(value):
    assert isinstance(value, (int, float)), "Input must be a number"
    assert value > 0, "Number must be positive"

    return str(value).count('0')

print(calculate_number_of_zeros(10), 'should be 1')
print(calculate_number_of_zeros(1070020394), 'should be 4')