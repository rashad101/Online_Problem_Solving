#https://leetcode.com/problems/two-sum/


#Runtime: 5828 ms, faster than 7.68% of Python online submissions for Two Sum.
#Memory Usage: 12.6 MB, less than 74.08% of Python online submissions for Two Sum.
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        length = len(nums)
        while (i < length - 1):
            j = i + 1
            while (j < length):
                if nums[i] + nums[j] == target:
                    return [i, j]
                j += 1
            i += 1
