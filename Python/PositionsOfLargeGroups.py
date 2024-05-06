class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        group_start = 0
        result = []
        i = 1
        while i < len(s):
            if s[i] != s[i - 1]:
                if i - group_start >= 3:
                    result.append([group_start, i - 1])
                group_start = i
            i += 1

        if i - group_start >= 3:
            result.append([group_start, i - 1])

        return result