class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        i = 0
        j = 0
        count = 0
        while i < len(grid) and grid[i][0] >= 0:
            while j < len(grid[0]) and grid[i][j] >= 0:
                j += 1

            count += (len(grid[0]) - j)
            j = 0

            i += 1

        count += (len(grid) - i) * len(grid[0])

        return count