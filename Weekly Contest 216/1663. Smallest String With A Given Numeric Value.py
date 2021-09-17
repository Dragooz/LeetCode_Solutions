class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        
        remainder = k % 26
        z_num = k // 26
        
        while remainder < n-z_num:
            z_num -= 1
            remainder += 26
            
        ans = 'z' * z_num
        
        if remainder - (n-z_num) != 0:
            ans += chr(ord('a') + remainder-(n-z_num)) #remainder - number of 'a' left
            
        ans += (n-len(ans)) * 'a'
        
        return ans[::-1]
            
        
        