class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        #   1) remove spaces from the end if there are spaces
        #   loop(last, first)
        #   2) count letters until space
        counter = 0

        j = len(s) - 1

        while j >= 0 and s[j] == ' ':
            j -= 1

        for i in range(j, -1, -1):
            if s[i] == ' ':
                return counter
            else:
                counter += 1

        return counter