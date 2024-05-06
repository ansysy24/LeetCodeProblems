def validMountainArray(arr) -> bool:

    if len(arr) < 3:
        return False

    i = 0

    while i + 1 < len(arr) and arr[i] < arr[i + 1]:
        i += 1

    if i == 0 or i + 1 == len(arr):
        return False
    else:
        while i + 1 < len(arr) and arr[i] > arr[i + 1]:
            i += 1

    return i + 1 == len(arr)

print(validMountainArray([1,2,3,4,5,4,3,2,1]))
print(validMountainArray([1,2,3,4,5,5,4,3,2,1]))
