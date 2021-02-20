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