def indexEqualsValue(array):
    if not array:
        return -1

    if len(array) - 1 > array[-1]:
        return -1

    left = 0
    right = len(array) - 1
    smallest = float('inf')
    while right - left > 1:
        test = int((left + right) // 2)
        if test == array[test]:
            smallest = min(smallest, test)
        if test <= array[test]:
            right = test
        else:
            left = test

    if left == array[left]:
        smallest = min(smallest, left)
    elif right == array[right]:
        smallest = min(smallest, right)
    return -1 if smallest == float('inf') else smallest

print(indexEqualsValue([-5, -3, 0, 3, 4, 5, 9]))