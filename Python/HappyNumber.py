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


class Solution2:
    def isHappy(self, n: int) -> bool:
        previous = {n}
        sm = 0
        for num in list(str(n)):
            sm += int(num) ** 2
        previous.add(sm)

        while sm != 1:
            new_sm = 0
            for num in list(str(sm)):
                new_sm += int(num) ** 2
            if new_sm in previous:
                return False
            previous.add(new_sm)
            sm = new_sm
        return True
