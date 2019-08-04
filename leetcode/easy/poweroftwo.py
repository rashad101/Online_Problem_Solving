#https://leetcode.com/problems/power-of-two/


#Runtime: 20 ms, faster than 61.06% of Python online submissions for Power of Two.
#Memory Usage: 11.7 MB, less than 62.64% of Python online submissions for Power of Two.
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