def maximum(value1, value2, value3):
    """Return the maximum of three values."""
    max_value = value1
    if value2 > max_value:
        max_value = value2
    if value3 > max_value:
        max_value = value3
    return max_value

def minimum(value1, value2, value3):
    """Return the minimum of three values."""
    min_value = value1
    if value2 < min_value:
        min_value = value2
    if value3 < min_value:
        min_value = value3
    return min_value

print(str(maximum(12, 27, 36)) + ' is the maximum, calculated with user defined maximum function')

print(str(max(12, 27, 36)) + ' is the maximum, calculated with built in max function')

print(str(minimum(15, 9, 27)) + ' is the minimum, calculated with user defined minimum function')

print(str(min(15, 9, 27)) + ' is the minimum, calculated with bult in min function')

print('Zach Fullers script ran successfully')