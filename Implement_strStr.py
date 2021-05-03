class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        i = 0
        while i <= len(haystack) - len(needle):
            j = i
            k = 0
            while j < len(haystack) and k < len(needle) and needle[k] == haystack[j]:
                j += 1
                k += 1

            if k == len(needle):
                return i
            i += 1
        return -1