class Solution:
    def maxProfit(self, prices) -> int:
        if len(prices) < 2:
            return 0
        i = 0
        while i < len(prices) - 1:
            if prices[i] == prices[i + 1]:
                prices.pop(i)
            else:
                i += 1

        if len(prices) < 2:
            return 0

        peaks = []
        if prices[1] > prices[0]:
            peaks.append(prices[0])

        for i in range(1, len(prices) - 1):
            if prices[i - 1] > prices[i] < prices[i + 1]:
                peaks.append(prices[i])
            elif prices[i - 1] < prices[i] > prices[i + 1]:
                peaks.append(prices[i])

        if prices[-1] > prices[-2]:
            peaks.append(prices[-1])

        i = 0
        profit = 0
        while i < len(peaks):
            profit -= peaks[i]
            i += 1
            profit += peaks[i]
            i += 1

        return profit


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        b = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > b:
                profit += prices[i] - b
            b = prices[i]

        return profit

