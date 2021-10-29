class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        
        ans = start
        
        for i in range(1, n):
            ans = ans ^ (start+2)
            start +=2

        return ans
        