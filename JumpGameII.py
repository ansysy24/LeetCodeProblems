class Solution:
    def jump(self, nums) -> int:
        self.memo = {}
        return self.jump1(nums)

    def jump1(self, nums) -> int:
        if len(nums) in self.memo:
            return self.memo[len(nums)]

        if len(nums) <= 1:
            return 0

        min_steps = len(nums) - 1
        for i in range(1, nums[0] + 1):
            min_steps = min(min_steps, self.jump1(nums[i:]) + 1)

        self.memo[len(nums)] = min_steps

        return min_steps