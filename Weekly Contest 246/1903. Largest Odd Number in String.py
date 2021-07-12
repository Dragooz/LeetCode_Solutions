class Solution(object):
    def largestOddNumber(self, num):
        """
        :type num: str
        :rtype: str
        """
        
        while num!= '':
            if int(num[-1]) % 2 == 1:
                return num
            else:
                num = num[:-1]
            
        return num