class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.perms = []
        self.helper(nums)
        return self.perms

    def helper(self, nums, current=[]):
        if not nums:
            self.perms.append(current)
        else:
            for i in range(len(nums)):
                self.helper(nums[:i] + nums[i + 1:], current + [nums[i]])