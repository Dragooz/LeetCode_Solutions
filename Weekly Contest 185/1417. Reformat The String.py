#Reference: https://leetcode.com/problems/reformat-the-string/discuss/586674/Python-Simple-solution

class Solution:
    def reformat(self, s: str) -> str:
        
        digits = []
        characters = []
        
        for char in s:
            if char.isdigit():
                digits.append(char)
            else:
                characters.append(char)
        
        ans = '' 
        
        if abs(len(digits) - len(characters))>1:
            return ''
        else:
            if len(digits) > len(characters):
                for i in range(len(digits) + len(characters)):
                    if i%2== 0:
                        ans+=str(digits[i//2])
                    else:
                        ans+=str(characters[i//2])
                        
            else:
                 for i in range(len(digits) + len(characters)):
                    if i%2== 0:
                        ans+=str(characters[i//2])
                    else:
                        ans+=str(digits[i//2])
                        
        return ans
            
        