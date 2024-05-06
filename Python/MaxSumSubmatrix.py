def maximumSumSubmatrix(matrix, size):
    max_matrix = float('-inf')
    i = 0
    while i < len(matrix)-size + 1:
        j = 0
        while j < len(matrix[0])-size + 1:
            current_sum = 0
            for k in range(i, i+size):
                for m in range(j, j+size):
                    current_sum += matrix[k][m]
            max_matrix = max(current_sum, max_matrix)
            j += 1
        i += 1
    return max_matrix