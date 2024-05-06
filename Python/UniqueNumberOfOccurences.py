class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dct = {}
        for num in arr:
            dct[num] = dct.get(num, 0) + 1

        lst = list(dct.values())

        return len(set(lst)) == len(lst)