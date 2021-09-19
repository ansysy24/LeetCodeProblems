# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 0
        right = n
        while left <= right:
            mid = (left + right) // 2
            bad_version = isBadVersion(mid)
            if bad_version:
                right = mid - 1
            elif not bad_version:
                left = mid + 1

        return left
