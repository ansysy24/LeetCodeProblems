def largestRange(array):
    array = list(set(array))
    array.sort()
    mx_range = (0, [0, 0])
    curr_len = 1
    curr_start = array[0]
    curr_end = array[0]
    for i, num in enumerate(array[:-1]):
        if num + 1 == array[i+1]:
            curr_len += 1
            curr_end += 1
        else:
            if curr_len > mx_range[0]:
                mx_range = (curr_len, [curr_start, curr_end])
                curr_len = 1
                curr_start = array[i+1]
                curr_end = array[i+1]
    if curr_len > mx_range[0]:
        return [curr_start, curr_end]
    return mx_range[1]


def largestRange2(array):
    s = {}
    max_range = 1
    result = [array[0], array[0]]

    for num in array:
        s[num] = True
    for i, num in enumerate(array):
        if s[num]:
            s[num] = False
            curr_range = 1

            k = 1
            while num - k in s:
                s[num - k] = False
                curr_range += 1
                k += 1


            m = 1
            while num + m in s:
                s[num + m] = False
                curr_range += 1
                m += 1

            if curr_range > max_range:
                max_range = curr_range
                result = [num - k + 1, num + m - 1 ]
    return result


print(largestRange([1,2,3,4,7,8,11,12]))
print(largestRange2([1,2,3,4,7,8,11,12]))