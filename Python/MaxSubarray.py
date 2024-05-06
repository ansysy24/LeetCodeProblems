class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current = 0
        result = nums[0]
        mn = 0
        for num in nums:
            current += num
            result = max(result, current - mn)
            mn = min(current, mn)

        return result