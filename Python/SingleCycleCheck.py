def hasSingleCycle(array):
    idx = 0
    count = 0
    while count <= len(array):
        idx = idx + array[idx]
        idx = idx%len(array)
        count += 1
        if idx == 0:
            return count == len(array)
    return False


print(hasSingleCycle([1, 2, 3, 4, -2, 3, 7, 8, -26]))