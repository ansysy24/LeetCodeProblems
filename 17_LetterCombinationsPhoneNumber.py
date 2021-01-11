from typing import List

class Solution:
    dct = {2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        self.lst = []
        word = ''
        for letter in self.dct[int(digits[0])]:
            self.helper(digits[1:], word + letter)
        return self.lst

    def helper(self, digits, word):

        if not digits:
            self.lst.append(word)
        else:
            for letter in self.dct[int(digits[0])]:
                self.helper(digits[1:], word + letter)

inst = Solution()
print(inst.letterCombinations('23'))
