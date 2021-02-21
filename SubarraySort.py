from bisect import bisect


def subarraySort(array):
    sorted = True

    for i, num in enumerate(array[:-1]):
        if num > array[i + 1]:
            sorted = False
            min_ind = i + 1
            min_num = array[i + 1]
            break

    if sorted:
        return [-1, -1]

    for i in range(min_ind + 1, len(array)):
        if array[i] < min_num:
            min_num = array[i]
            min_ind = i

    final_min_ind = bisect(array, min_num, hi=min_ind)

    for i in range(len(array) - 1, 0, -1):
        if array[i] < array[i - 1]:
            max_num = array[i - 1]
            max_ind = i - 1
            break

    for i in range(max_ind - 1, -1, -1):
        if array[i] > max_num:
            max_num = array[i]
            max_ind = i

    final_max_ind = bisect(array, max_num, lo=max_ind) - 1

    return [final_min_ind, final_max_ind]

print(subarraySort([1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]))