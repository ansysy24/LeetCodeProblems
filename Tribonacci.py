class Solution:
    def tribonacci(self, n: int) -> int:

        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 1

        lst = [0 for i in range(n + 1)]
        lst[1] = 1
        lst[2] = 1

        for j in range(3, n + 1):
            lst[j] = lst[j - 1] + lst[j - 2] + lst[j - 3]

        return lst[-1]