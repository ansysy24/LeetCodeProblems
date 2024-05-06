# N*N
# What are a total # of ways you can move from top-left cell to the bottom-right cell
# A[0][0] -> A[n - 1][n - 1]
# Given that you can move only downward or rightward
#
# 1 2 3
# 4 5 6
# 7 8 9

# Recursive solution
def total_ways(row, col) -> int:
    if row == 0 and col == 0:
        return 0
    elif row == 0:
        return 1
    elif col == 0:
        return 1
    return total_ways(row, col-1) + total_ways(row-1, col)




# total_ways(2,2)
# total_ways(2, 1) | total_ways(1, 2)
# total_ways(1, 1) | total_ways(2, 0) | total_ways(0, 2) | total_ways(1, 1)
# [0, 1, 1]
# [1, 2, 3]
# [1, 3, 6]

# row1 [0, 1, 1]

# Dynamic programming with optimized memory
def total_ways2(row, col) -> int:
    row1 = [1 for n in range(col+1)]
    row1[0] = 0

    row2 = [1 for n in range(col+1)]

    j = row

    while j:
        for i in range(1, row+1):
            row2[i] = row2[i-1] + row1[i]

        j -= 1
        row1 = row2
        print(row1)

    return row2[-1]

print(total_ways2(2, 2))