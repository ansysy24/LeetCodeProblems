class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        prev = [1]*rowIndex + [1]
        current = [1]*rowIndex + [1]

        for j in range(2, rowIndex+1):
            for i in range(1, j):
                current[i] = prev[i-1] + prev[i]
            prev = current[:]

        return prev
