class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows = numRows
        if rows == 1:
            return s

        cols1 = (len(s) // (rows + rows - 2)) * (rows - 1)
        pre_cols2 = len(s) % (rows + rows - 2)
        cols2 = 0
        if 0 < pre_cols2 <= rows:
            cols2 = 1
        elif pre_cols2 > rows:
            cols2 = 1 + pre_cols2 - rows

        cols = cols1 + cols2
        matrix = [[0 for c in range(cols)] for r in range(rows)]

        ind = 0
        j = 0
        while j < cols:

            if j % (rows - 1) == 0:
                for i in range(rows):

                    if ind < len(s):
                        matrix[i][j] = s[ind]
                        ind += 1
                j += 1
                i -= 1
            else:

                while i > 0 and ind < len(s):
                    print(i, j, ind)
                    matrix[i][j] = s[ind]
                    ind += 1
                    i -= 1
                    j += 1

        result = ''
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                result += matrix[i][j] if matrix[i][j] else ''

        return result