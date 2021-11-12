class Solution:
    def maxPower(self, s: str) -> int:
        
        temp = s[0]
        final_ans = 1
        ans = 1
        for char in s[1:]:
            if temp == char:
                ans+=1 
            else:
                final_ans =  max(final_ans, ans)
                temp = char
                ans=1
                
        return max(final_ans, ans)