#https://leetcode.com/problems/powx-n/

#Runtime: 8 ms, faster than 99.40% of Python online submissions for Pow(x, n).
#Memory Usage: 11.9 MB, less than 23.40% of Python online submissions for Pow(x, n).

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        import math
        return float("{0:.5f}".format(math.pow(x,n)))
