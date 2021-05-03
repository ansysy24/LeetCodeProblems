class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)
        while end - start > 1:
            mid = (start + end) // 2

            if target == nums[mid]:
                return mid

            elif target < nums[mid]:
                end = mid
            else:
                start = mid

        if target <= nums[start]:
            return start
        else:
            return end