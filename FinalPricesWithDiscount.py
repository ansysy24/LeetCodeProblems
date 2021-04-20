class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        answer = []
        for i, price in enumerate(prices):
            current = 0
            for price2 in prices[i+1:]:
                if price2 <= price:
                    current = price2
                    break
            answer.append(price-current)
        return answer