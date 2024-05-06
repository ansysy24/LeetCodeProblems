class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        z = 0
        i = 0
        while z < len(nums):
            while nums[z] == 0 and z < len(nums) - 1:
                z += 1
            nums[i] = nums[z]
            i += 1
            z += 1

        for j in range(i, len(nums)):
            nums[j] = 0