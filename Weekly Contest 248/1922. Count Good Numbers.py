'''
References:
https://leetcode.com/problems/count-good-numbers/discuss/1314434/Python%3A-Logarithmic-Time-Solution by meaditya70
'''

class Solution(object):
    def countGoodNumbers(self, n):
        """
        :type n: int
        :rtype: int
        """
        num=1
        n_range = n/2 #as its 5x4x5...x5, so can consider it as 20x20x....x5 (if odd)
        
        x = 20
        mod = 10**9 + 7
        
        #pow algorithm
        while n_range!=0 :
            if n_range%2 ==1:
                num = num * x % mod
            n_range = n_range / 2
            x = x * x % mod
                
        #if even, then its correct
        #if odd, then multiply by 5 to satisfy the eq.
        if n%2 == 0:#even
            return num
        else:
            return num*5 % mod