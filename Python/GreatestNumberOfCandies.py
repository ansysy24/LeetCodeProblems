from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        mx = max(candies)
        result = []
        for kid_has in candies:
            result += [False] if kid_has + extraCandies < mx else [True]

        return result
