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

# DP solution:
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if not cost:
            return 0
        elif len(cost) == 1:
            return cost[0]

        dist = [0] * (len(cost) + 1)

        for i in range(2, len(cost) + 1):
            dist[i] = min(dist[i - 2] + cost[i - 2], dist[i - 1] + cost[i - 1])

        return dist[-1]