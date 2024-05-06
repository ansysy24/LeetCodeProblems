class Solution:
    def generateParenthesis(self, n: int):

        self.answer = []
        self.helper('(', n - 1, n)

        return self.answer

    def helper(self, cur_str, opening, closing):
        if opening == 0 and closing == 0:
            self.answer.append(cur_str)

        if opening > 0:
            self.helper(cur_str + '(', opening - 1, closing)
        if closing - opening > 0:
            self.helper(cur_str + ')', opening, closing - 1)