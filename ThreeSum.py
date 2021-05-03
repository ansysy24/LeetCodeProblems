class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = set()
        for i in range(len(nums)-2):
            start = i+1
            end = len(nums)-1
            while start<end:
                if nums[i] + nums[start] + nums[end] < 0:
                    start += 1
                elif nums[i] + nums[start] + nums[end] > 0:
                    end -= 1
                else:
                    new_add = (nums[i], nums[start], nums[end])
                    result.add(new_add)
                    start += 1
                    end -= 1
        result = [list(x) for x in result]
        return result