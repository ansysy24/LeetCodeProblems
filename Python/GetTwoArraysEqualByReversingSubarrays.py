class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        dct = {}
        for num in target:
            dct[num] = dct.get(num, 0) + 1

        for num2 in arr:
            if num2 in dct and dct[num2] > 0:
                dct[num2] -= 1
            else:
                return False
        return True