class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_count = collections.Counter(s)
        t_count = collections.Counter(t)
        print(t_count, s_count)
        for key in t_count:
            if t_count.get(key) != s_count.get(key):
                return key