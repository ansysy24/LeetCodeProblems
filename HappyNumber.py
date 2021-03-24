class Solution:
    def isHappy(self, n: int) -> bool:
        n = str(n)
        s = {n}
        while True:
            a = 0
            for digit in n:
                a += int(digit) ** 2

            n = str(a)
            if n == '1':
                return True
            if n in s:
                return False
            else:
                s.add(n)