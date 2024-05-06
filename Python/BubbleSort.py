def bubbleSort(array):
    j = -1
    isSorted = False
    while not isSorted:
        isSorted = True
        for i in range(len(array)-1, j, -1):
            if array[i] < array[i-1]:
                array[i], array[i-1] = array[i-1], array[i]
                isSorted = False
        j += 1
    return array

print(bubbleSort([1,4,4,4,5,6,7,3,4,5,6,7,3,4,1,3,4,5,6,7,8,9]))