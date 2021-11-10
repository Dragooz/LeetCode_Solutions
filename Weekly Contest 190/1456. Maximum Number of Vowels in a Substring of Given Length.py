#Reference: https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/discuss/648559/JavaPython-3-Slide-Window-O(n)-codes.

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        vowel = ['a', 'e', 'i', 'o', 'u']
        ans = 0
        vowel_num = 0
        index = 0
        
        for char in s:
            if char in vowel:
                vowel_num += 1
            
            if index >= k and s[index-k] in vowel:
                vowel_num-=1
                
            ans = max(ans, vowel_num)
            index+=1
                
        return ans
            
            
            