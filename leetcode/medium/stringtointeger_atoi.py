#https://leetcode.com/problems/string-to-integer-atoi/

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        import math
        num = str.strip().split(" ")
        if len(num) == 0:
            return 0
        try:
            if "." in num[0]:
                num = float(num[0])
                num = round(num)
            else:
                num = int(num[0])

            if num > (math.pow(2, 31) - 1):
                return int(math.pow(2, 31) - 1)
            elif num < -1 * math.pow(2, 31):
                return int(-1 * math.pow(2, 31))
            else:
                return int(num)
        except ValueError:
            return 0