class Solution2:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        triangle.reverse()
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                triangle[i][j] = triangle[i][j] + min(triangle[i-1][j], triangle[i-1][j+1])
        return triangle[-1][0]

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle) == 1:
            return triangle[0][0]

        elif len(triangle) == 2:
            return triangle[0][0] + min(triangle[1][0], triangle[1][1])

        else:
            dp = triangle[:]

            for i in range(1, len(triangle)):
                dp[i][0] += dp[i - 1][0]

            for i in range(1, len(triangle)):
                dp[i][len(dp[i]) - 1] += dp[i - 1][len(dp[i - 1]) - 1]

            for i in range(2, len(triangle)):
                for j in range(1, len(triangle[i])):
                    if j == len(triangle[i]) - 1:
                        continue
                    else:
                        dp[i][j] += min(dp[i - 1][j], dp[i - 1][j - 1])

            return min(dp[len(dp) - 1])