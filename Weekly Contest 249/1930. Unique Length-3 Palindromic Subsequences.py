#Reference:
#https://leetcode.com/problems/unique-length-3-palindromic-subsequences/discuss/1330178/Python-Straight-Forward-Solutionby lee215

class Solution(object):
    def countPalindromicSubsequence(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        #main idea: find the same char on the beginning and end of the string
        #then every unique char in between will be the palindrome of 3
        #count and return the sum
        ans = 0
        for char in string.ascii_lowercase:
            i, j = s.find(char), s.rfind(char) 
            
            if (i != -1 and j !=-1) or i!=j: #found
                ans += len(set(s[i+1:j])) #unique value in between
        
        return ans