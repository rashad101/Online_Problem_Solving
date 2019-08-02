#https://leetcode.com/problems/single-number/


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
        
