#https://leetcode.com/problems/search-insert-position/


#Runtime: 36 ms, faster than 68.80% of Python online submissions for Search Insert Position.
#Memory Usage: 12.1 MB, less than 96.79% of Python online submissions for Search Insert Position.
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i,n in enumerate(nums):
            if i==0:
                if nums[i]==target:
                    return i
                elif len(nums)==1:
                    if nums[i]>target:
                        return 0
                    elif nums[i]==target:
                        return i
                    else:
                        return i+1
                if nums[i]>target:
                    return 0
            elif i==len(nums)-1:
                if nums[i]==target:
                    return i
                elif nums[i]>target:
                    return i
                else:
                    return i+1
            else:
                if nums[i]==target:
                    return i
                elif nums[i]>target:
                    return i