class Solution:
    def minOperations(self, n: int) -> int:
        
        if n%2 == 0:
            return sum( (i*2)+1 for i in range(0, n//2))
        else:
            return sum( (i*2) for i in range(1 , (n//2) +1 ))
