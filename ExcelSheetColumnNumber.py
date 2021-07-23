class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        dct = {letter:i+1 for i, letter in enumerate(letters)}
        value = 0
        i = len(columnTitle)-1
        n = 0
        while i >= 0:
            value += pow(26, n)*dct[columnTitle[i]]
            n += 1
            i -= 1
        return value