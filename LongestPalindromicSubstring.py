class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = 1
        result = s[0]
        odd_pals_i = []
        even_pals_i = []
        for i in range(1, len(s) - 1):
            if s[i - 1] == s[i + 1]:
                odd_pals_i.append(i)

        for pal in odd_pals_i:
            cur_len = 3
            j = 2
            while pal - j > -1 and pal + j < len(s) and s[pal - j] == s[pal + j]:
                cur_len += 2
                j += 1

            if cur_len > longest:
                longest = cur_len
                result = s[pal - j + 1:pal + j]

        for i in range(1, len(s)):
            if s[i - 1] == s[i]:
                even_pals_i.append(i)

        for pal in even_pals_i:
            cur_len = 2
            k = 1
            while pal - k - 1 > -1 and pal + k < len(s) and s[pal - k - 1] == s[pal + k]:
                cur_len += 2
                k += 1

            if cur_len > longest:
                longest = cur_len
                result = s[pal - k:pal + k]

        return result