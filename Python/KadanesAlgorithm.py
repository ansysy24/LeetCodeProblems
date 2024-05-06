def kadanesAlgorithm(array):
    mx_here = array[0]
    mx = array[0]
    for num in array[1:]:
        mx_here = max(num, mx_here + num)
        mx = max(mx, mx_here)
    return mx


def kadanesAlgorithm2(array):
    sm = array[0]
    mn = 0 if array[0] > 0 else array[0]
    mx = array[0]
    for num in array[1:]:
        sm += num
        mx = max(mx, sm - mn)
        mn = min(mn, sm)
    return mx

print(kadanesAlgorithm([3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]))
print(kadanesAlgorithm2([3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]))