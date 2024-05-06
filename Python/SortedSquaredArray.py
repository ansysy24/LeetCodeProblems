def sortedSquaredArray(array):
    left = 0
    right = len(array) - 1
    squares = []
    while left < right:
        if abs(array[left]) > abs(array[right]):
            squares = [array[left] * array[left]] + squares
            left += 1
        elif array[left] == array[right]:
            squares = [array[left] * array[left], array[left] * array[left]] + squares
            left += 1
            right -= 1

        else:
            squares = [array[right] * array[right]] + squares
            right -= 1

    if left == right:
        squares = [array[left] * array[left]] + squares

    return squares

print(sortedSquaredArray([-50, -13, -2, -1, 0, 0, 1, 1, 2, 3, 19, 20]))