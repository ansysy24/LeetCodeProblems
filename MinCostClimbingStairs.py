class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        self.memo = {}
        return self.helper(cost)

    def helper(self, cost):

        if tuple(cost) in self.memo:
            return self.memo[tuple(cost)]

        if len(cost) < 2:
            return 0

        self.memo[tuple(cost)] = min(self.helper(cost[1:]) + cost[0],
                                     self.helper(cost[2:]) + cost[1])

        return self.memo[tuple(cost)]