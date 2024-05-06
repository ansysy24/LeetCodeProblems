def insertionSort(array):
    j = 1
    while j < len(array):
        i = j
        while i > 0 and array[i-1] > array[i]:
            array[i-1], array[i] = array[i], array[i-1]
            i -= 1
        j += 1
    return array

print(insertionSort([1,2,3,7,5,3,2,1,8,0,-8,-8,-8,-5,-23, 0, 56, 45, 3, 2, 1,]))

