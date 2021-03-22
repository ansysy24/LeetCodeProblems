class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if not strs:
            return ''
        i = 0
        longest = ''
        while True:
            if i == len(strs[0]):
                return longest
            current_letter = strs[0][i]
            for word in strs[1:]:
                if i == len(word) or current_letter != word[i]:
                    return longest

            longest += current_letter

            i += 1

S = Solution()

print(S.longestCommonPrefix(["flower","flow","flight"]))