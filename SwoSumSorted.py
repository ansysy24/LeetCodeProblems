class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 1
        end = len(numbers)
        while start < end:
            if numbers[start-1] + numbers[end-1] == target:
                return [start, end]
            elif numbers[start-1] + numbers[end-1] < target:
                start += 1
            else:
                end -= 1