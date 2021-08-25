class Solution:
    def reverseVowels(self, s: str) -> str:
        l = 0
        r = len(s) - 1
        lst = list(s)
        while l < r:
            if lst[l] not in 'uioaeUIOAE':
                l += 1
                continue
            if lst[r] not in 'uioaeUIOAE':
                r -= 1
                continue

            lst[l], lst[r] = lst[r], lst[l]
            l += 1
            r -= 1
        return ''.join(lst)