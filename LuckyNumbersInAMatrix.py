class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        mns = set()
        result = []
        for row in matrix:
            mns.add(min(row))
        for i in range(len(matrix[0])):
            mx = max([matrix[j][i] for j in range(len(matrix))])
            if mx in mns:
                result.append(mx)
        return result