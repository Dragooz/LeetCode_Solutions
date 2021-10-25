class Solution:
    def numSub(self, s: str) -> int:
        
        splitted = [i for i in s.split('0') if i!='']
        
        ans = 0
        
        for sp in splitted:
            temp = 0
            for i in range(1, len(sp)+1):
                temp += i
            ans+=temp
            
        return ans % ((10**9) + 7)