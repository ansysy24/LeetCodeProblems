class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        counter = 0
        for i in range(len(strs[0])):
            list2 = sorted(strs, key = lambda x: x[i])
            counter += 1 if list2 != strs else 0
        return counter