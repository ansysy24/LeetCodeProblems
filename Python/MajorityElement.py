class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None
        for element in nums:
            if count == 0:
                candidate = element
            count += 1 if element == candidate else -1

        return candidate
