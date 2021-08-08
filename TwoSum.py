class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dct = {}
        for i, num in enumerate(nums):
            if target-num in dct:
                return (dct[target-num], i)
            dct[num] = i