#https://leetcode.com/problems/power-of-two/

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """

        if n == 1 or n == 2:
            return True

        if n % 2 != 0 or n == 0:
            return False

        while (n != 1):
            if n % 2 == 0:
                n = n // 2
            else:
                return False

        return True