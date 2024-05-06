class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.perms = set()
        self.helper(nums)
        return self.perms

    def helper(self, nums, cur_perm=[]):
        if not nums:
            self.perms.add(tuple(cur_perm))
        else:
            for i, num in enumerate(nums):
                self.helper(nums[:i] + nums[i + 1:], cur_perm + [num])