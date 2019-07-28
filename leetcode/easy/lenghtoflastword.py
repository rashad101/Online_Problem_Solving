#https://leetcode.com/problems/length-of-last-word/


#Runtime: 16 ms, faster than 76.67% of Python online submissions for Length of Last Word.
#Memory Usage: 12 MB, less than 26.14% of Python online submissions for Length of Last Word.
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        if s.strip() == "":
            return 0
        words = s.strip().split()
        return len(words[len(words) - 1])

