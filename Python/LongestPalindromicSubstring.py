class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = 1
        result = s[0]

        for i in range(1, len(s) - 1):
            if s[i - 1] == s[i + 1]:
                cur_len = 3
                j = 2
                while i - j > -1 and i + j < len(s) and s[i - j] == s[i + j]:
                    cur_len += 2
                    j += 1

                if cur_len > longest:
                    longest = cur_len
                    result = s[i - j + 1:i + j]

        for i in range(1, len(s)):
            if s[i - 1] == s[i]:
                cur_len = 2
                k = 1
                while i - k - 1 > -1 and i + k < len(s) and s[i - k - 1] == s[i + k]:
                    cur_len += 2
                    k += 1

                if cur_len > longest:
                    longest = cur_len
                    result = s[i - k:i + k]

        return result