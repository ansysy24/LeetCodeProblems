class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total_sum = int(len(nums)*(len(nums)+1)/2)
        for num in nums:
            total_sum -= num
        return total_sum