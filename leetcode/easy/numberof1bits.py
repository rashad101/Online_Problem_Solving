#https://leetcode.com/problems/number-of-1-bits/submissions/

#Runtime: 16 ms, faster than 80.88% of Python online submissions for Number of 1 Bits.
#Memory Usage: 11.8 MB, less than 18.61% of Python online submissions for Number of 1 Bits.
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        n = bin(n)[2:]
        binstring = str(n)
        count = 0
        for i in range(len(binstring)):
            if binstring[i]=="1":
                count+=1
        return count