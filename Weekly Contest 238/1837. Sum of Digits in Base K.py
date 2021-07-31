class Solution:
    def sumBase(self, n: int, k: int) -> int:
        #convert to base k
        #get the sum
        
        ans = ''
        while n > 0:
            ans = str(n%k) + ans
            n = n//k
            
        return sum(int(a) for a in ans)