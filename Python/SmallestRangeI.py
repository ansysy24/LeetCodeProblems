class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        min_ = float('inf')
        max_ = float('-inf')

        for num in nums:
            min_ = min(min_, num)
            max_ = max(max_, num)

        result = max_ - min_ - 2 * k

        return result if result > 0 else 0