# input n = 3
# output 3
# 3
# 1 2
# 1 1 0


class Solution:
    memo = {}

    def climbStairs(self, n: int) -> int:
        if n in self.memo:
            return self.memo[n]

        if n < 2:
            return 1

        self.memo[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)

        return self.memo[n]