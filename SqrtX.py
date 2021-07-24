# 0--------10
# mid = 5
# end = 5

class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        start = 0
        end = x

        while start < end:
            mid = (start + end) // 2
            if mid * mid == x:
                return mid

            if mid * mid > x:
                end = mid

            elif mid * mid < x:
                if (mid + 1) * (mid + 1) > x:
                    return mid
                else:
                    start = mid