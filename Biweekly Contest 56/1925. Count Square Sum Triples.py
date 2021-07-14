'''
References:
https://leetcode.com/problems/count-square-sum-triples/discuss/1329355/O(n2)-C%2B%2BJavaPython by lokeshsenthilkumar
'''

class Solution(object):
    def countTriples(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        for i in range(1, n):
            for j in range(i+1, n+1):
                
                squared = i**2 + j**2
                
                if (squared**0.5) - int(squared**0.5) == 0 and squared <= n**2: #square exist and smaller/equal to n^2
                    ans +=2 
                    
        return ans