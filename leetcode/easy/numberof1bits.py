#https://leetcode.com/problems/number-of-1-bits/submissions/


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