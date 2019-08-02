#https://leetcode.com/problems/single-number/

#Runtime: 64 ms, faster than 91.59% of Python online submissions for Single Number.
#Memory Usage: 14.8 MB, less than 8.59% of Python online submissions for Single Number.
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mapping = dict()
        
        for a in nums:
            if a in mapping:
                mapping[a]+=1
            else:
                mapping[a] = 1
                
        for k,_ in mapping.items():
            if mapping[k]==1:
                return k
        
