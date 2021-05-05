import itertools
class Solution:
    def minFlips(self, target: str) -> int:
        i = itertools.groupby(target)
        counter = 0
        for i, group in enumerate(i):
            if i == 0:

                counter = 1 if group[0]=='1' else 0
            else:
                counter += 1

        return counter