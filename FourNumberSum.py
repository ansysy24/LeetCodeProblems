def fourNumberSum(array, target):
    quadr = []
    pairs = {}

    for i in range(1, len(array) - 1):
        for j in range(i + 1, len(array)):
            correspond = target - array[i] - array[j]
            if correspond in pairs:
                for pair in pairs[correspond]:
                    quadr.append(pair + [array[i]] + [array[j]])

        for k in range(i):
            pairs[array[k] + array[i]] = pairs.get(array[k] + array[i], []) + [[array[k], array[i]]]

    return quadr


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        quads = set()
        nums.sort()
        for i in range(len(nums) - 3):
            for j in range(i + 1, len(nums) - 2):
                for k in range(j + 1, len(nums) - 1):
                    for l in range(k + 1, len(nums)):
                        if nums[i] + nums[j] + nums[k] + nums[l] == target:
                            quads.add((nums[i], nums[j], nums[k], nums[l]))

        return quads