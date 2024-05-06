class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        output = [[1]*n for n in range(1,numRows+1)]
        for i in range(2, numRows):
            ln = len(output[i])
            for j in range(1, ln-1):
                output[i][j] = output[i-1][j-1] + output[i-1][j]
        return output