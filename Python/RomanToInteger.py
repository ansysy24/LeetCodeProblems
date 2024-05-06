# LXIX

class Solution:
    def romanToInt(self, s: str) -> int:
        dct = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        mx = 0
        result = 0
        i = len(s) - 1
        while i > -1:
            cur_num = dct[s[i]]
            mx = max(mx, cur_num)
            result = result + cur_num if cur_num == mx else result - cur_num
            i -= 1

        return result