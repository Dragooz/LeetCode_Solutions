#Reference: https://leetcode.com/problems/four-divisors/discuss/1017330/Easy-and-Clear-Solution-Python-3

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        
        ans = 0
        
        for i in nums:
            x = set()
            for d in range(1, floor(sqrt(i)) + 1):
                if i%d == 0:
                    x.add(d)
                    x.add(i//d)
                    
                if len(x) > 4:
                    break
            
            if len(x) == 4:
                ans += sum(x)
            
        return ans