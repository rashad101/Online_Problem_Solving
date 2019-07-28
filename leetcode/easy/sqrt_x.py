#https://leetcode.com/problems/sqrtx/

#Runtime: 24 ms, faster than 63.90% of Python online submissions for Sqrt(x).
#Memory Usage: 11.8 MB, less than 56.36% of Python online submissions for Sqrt(x).
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        import math
        return int(math.sqrt(x))