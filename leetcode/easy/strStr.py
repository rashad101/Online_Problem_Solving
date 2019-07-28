#https://leetcode.com/problems/implement-strstr/

#Runtime: 16 ms, faster than 84.29% of Python online submissions for Implement strStr().
#Memory Usage: 12.1 MB, less than 38.07% of Python online submissions for Implement strStr().
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return haystack.find(needle)