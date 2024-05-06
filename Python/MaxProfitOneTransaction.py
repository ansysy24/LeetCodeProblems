class Solution:
    def maxProfit(prices) -> int:
        maximums = [0 for _ in prices]
        mx = prices[-1]
        maximums[-1] = mx
        for i in range(len(prices) - 2, -1, -1):
            mx = max(mx, prices[i])
            maximums[i] = mx

        profit = 0
        for i, price in enumerate(prices):
            profit = max(profit, maximums[i] - price)

        return profit


class Solution2:
    def maxProfit(prices) -> int:
        if len(prices) < 2:
            return 0
        mn = prices.pop(0)
        profit = 0
        for price in prices:
            profit = max(profit, price - mn)
            mn = min(mn, price)

        return profit


print(Solution2.maxProfit([7, 1, 5, 3, 6, 4]))
print(Solution.maxProfit([7, 1, 5, 3, 6, 4]))
