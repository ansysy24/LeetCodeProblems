def GFG(a):
    max_so_far = float("-inf")
    max_here = 0
    for i in range(len(a)):
        max_here += a[i]
        max_so_far = max(max_so_far, max_here)
        max_here = max(max_here, 0)
    return max_so_far

# Driver function to check the above function
a = [-2, -3, -4, -1, -2, -1, -5, -3]
print("Maximum contiguous sum is", GFG(a))

