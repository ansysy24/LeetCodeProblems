class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dct_s = {}
        dct_t = {}

        for i in range(len(s)):
            if s[i] not in dct_s and t[i] not in dct_t:
                dct_s[s[i]] = i
                dct_t[t[i]] = i
            elif (s[i] in dct_s and t[i] not in dct_t) or (s[i] not in dct_s and t[i] in dct_t):
                return False
            elif s[i] in dct_s and t[i] in dct_t and dct_s[s[i]] != dct_t[t[i]]:
                return False
        return set(dct_t.values()) == set(dct_s.values())