class Solution:

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        self.memo = {}
        ht = len(obstacleGrid) - 1
        wd = len(obstacleGrid[0]) - 1
        return self.helper(obstacleGrid, ht, wd)

    def helper(self, matrix, ht, wd):
        if (ht, wd) in self.memo:
            return self.memo[(ht, wd)]

        if matrix[ht][wd]:
            return 0

        if ht == 0 and wd == 0:
            return 1

        next_ht = 0
        next_wd = 0

        if ht > 0:
            next_ht = self.helper(matrix, ht - 1, wd)
        if wd > 0:
            next_wd = self.helper(matrix, ht, wd - 1)

        self.memo[(ht, wd)] = next_ht + next_wd

        return next_ht + next_wd