def flip(arr, k):
    temp = []
    i = 0
    while arr and i < k:
        current = arr.pop(0)
        temp = [current] + temp
        i += 1
    return temp + arr


def pancake_sort(arr):
    for j in range(len(arr)):
        largest = 0
        for i in range(len(arr) - j):
            if arr[i] > arr[largest]:
                largest = i
        arr = flip(arr, largest + 1)
        arr = flip(arr, len(arr) - j)
    return arr

print(pancake_sort([9, 1, 3, 5, 8, 2, 4, 7, 6]))