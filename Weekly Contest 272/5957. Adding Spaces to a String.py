class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        
        ans = ''
        temp = 0
        
        for num, space in enumerate(spaces):
            ans += s[temp:space] + ' '
            temp = len(ans) - (num+1) 

            
        return ans + s[spaces[-1]:]