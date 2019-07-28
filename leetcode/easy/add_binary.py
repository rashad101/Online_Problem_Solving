#https://leetcode.com/problems/add-binary/

#Runtime: 20 ms, faster than 81.64% of Python online submissions for Add Binary.
#Memory Usage: 11.8 MB, less than 31.13% of Python online submissions for Add Binary.
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        sm = int(a,2)+int(b,2)
        return bin(sm)[2:]