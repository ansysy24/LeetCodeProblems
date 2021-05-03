class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        dct = {}
        sm = 0
        for num in nums:
            dct[num] = dct.get(num, 0) + 1
            if dct[num] == 1:
                sm += num
            elif dct[num] == 2:
                sm -= num

        return sm