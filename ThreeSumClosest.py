class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()

        diff = float('inf')
        result = float('inf')
        min_diff = float('inf')

        for i in range(len(nums) - 2):
            num1 = nums[i]
            start = i + 1
            end = len(nums) - 1

            while start < len(nums) - 1 and end > i + 1 and start < end:
                num2 = nums[start]
                num3 = nums[end]
                cur_sum = num1 + num2 + num3

                if cur_sum == target:
                    return cur_sum
                elif cur_sum < target:
                    start += 1
                else:
                    end -= 1

                diff = abs(cur_sum - target)

                if diff < min_diff:
                    min_diff = diff
                    result = cur_sum

        return result