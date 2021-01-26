def longestPeak(array):
    peaks = []
    for i in range(1, len(array)-1):
        if array[i-1] < array[i] and array[i] > array[i+1]:
            peaks.append(i)
    mx = 0
    for j in peaks:
        left = 0
        k = j
        while k > 0 and array[k-1] < array[k]:
            left += 1
            k -= 1
        right = 0
        k = j
        while k < len(array)-1 and array[k+1] < array[k]:
            right += 1
            k += 1
        mx = max(mx, left+right+1)
    return mx

print(longestPeak([1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]))