class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
   
        n = len(word1)
        m = len(word2)   
            
        if len(word1) < len(word2):
            word1 += 'A' * abs(n-m)
        else:
            word2 += 'A' * abs(n-m)
            
        ans = ''
        for a, b in zip(word1, word2):
            
            if a != 'A':
                ans+= a
            if b != 'A':
                ans+= b
            
        return ans