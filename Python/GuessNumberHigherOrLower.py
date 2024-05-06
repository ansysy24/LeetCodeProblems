# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left = 0
        right = n
        while left <= right:
            middle = (left+right)//2
            if guess(middle) == 0:
                return middle
            elif guess(middle) == 1:
                left = middle + 1
            else:
                right = middle - 1
