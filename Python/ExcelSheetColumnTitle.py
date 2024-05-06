class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        dct = {i + 1: letter for i, letter in enumerate(letters)}
        result = ''
        while columnNumber > 26:
            if columnNumber % 26 > 0:
                current_letter = dct[columnNumber % 26]
                carryover = 0
            else:
                current_letter = 'Z'
                carryover = 1
            result = current_letter + result
            columnNumber = columnNumber // 26 - carryover

        return dct[columnNumber] + result