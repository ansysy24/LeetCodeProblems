class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        last_seen = {}
        result_len = 0
        for end, char in enumerate(s):
            if char in last_seen:
                start = max(start, last_seen[char] + 1)

            last_seen[char] = end
            result_len = max(result_len, end-start+1)

        return result_len