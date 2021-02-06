def threeNumberSort(array, order):
    idx = 0
    for i in range(len(array)):
        if array[i] == order[0]:
            array[i], array[idx] = array[idx], array[i]
            idx += 1
    idx = len(array) - 1
    for i in range(len(array)-1, -1, -1):
        if array[i] == order[2]:
            array[i], array[idx] = array[idx], array[i]
            idx -= 1
    return array


print(threeNumberSort([1, 0, 0, -1, -1, 0, 1, 1], [0, 1, -1]))
