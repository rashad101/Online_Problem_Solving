#https://leetcode.com/problems/reverse-integer/s

#Runtime: 24 ms, faster than 42.87% of Python online submissions for Reverse Integer.
#Memory Usage: 11.8 MB, less than 51.29% of Python online submissions for Reverse Integer.
class Solution(object):
    def reverse(self, x):
        if x >= 0:
            x = int(str(x)[::-1])
        else:
            num = str(x)[1:]
            num = num[::-1]
            x = int(num) * (-1)

        if x > 2147483647 or x < -2147483648:
            return 0
        else:
            return x
