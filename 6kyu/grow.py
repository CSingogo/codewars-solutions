"""

Given a non-empty array of integers, return the result of multiplying the values together in order. Example:

[1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24

"""

#solution

def grow(arr):
    length = len(arr)
    product = 1;
    for i in range(length):
        product *= arr[i]
    return product