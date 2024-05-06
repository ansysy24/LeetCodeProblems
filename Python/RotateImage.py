class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if len(matrix)<2:
            return matrix
        ln = len(matrix)-1
        for n in range(len(matrix)//2):
            for i in range(n, ln-n):
                matrix[n][i], matrix[i][ln-n], matrix[ln-n][ln-i], matrix[ln-i][n] =\
                    matrix[ln-i][n], matrix[n][i], matrix[i][ln-n], matrix[ln-n][ln-i]