def selectionSort(array):
    j = 0
    while j < len(array) - 1:
        mn_ind = j
        for i in range(j + 1, len(array)):
            if array[i] < array[mn_ind]:
                mn_ind = i
        array[j], array[mn_ind] = array[mn_ind], array[j]
        j += 1
    return array

print(selectionSort([1, 4, 4, 4, 5, 6, 7, 3, 4, 5, 6, 7, 3, 4, 1, 3, 4, 5, 6, 7, 8, 9]))
