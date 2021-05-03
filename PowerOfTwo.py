class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 0:
            return False

        n = bin(n)[2:]

        if n == '1':
            return True
        elif n == '0':
            return False

        return all([digit == '0' for digit in n[1:]])