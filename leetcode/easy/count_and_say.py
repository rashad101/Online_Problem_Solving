#https://leetcode.com/problems/count-and-say/


class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        numlist = ["1"]
        prev = "1"
        for i in range(1,31,1):
            chk = numlist[i-1]
            newgen = ""
            current_char = chk[0]
            ct = 0
            if i>n:
                break
            for j in range(len(chk)):
                if chk[j]==current_char:
                    ct+=1
                else:
                    newgen+=str(ct)+current_char
                    current_char = chk[j]
                    ct=1
                if j==len(chk)-1:
                    newgen += str(ct) + current_char
                    numlist.append(newgen)

        return numlist[n-1]
