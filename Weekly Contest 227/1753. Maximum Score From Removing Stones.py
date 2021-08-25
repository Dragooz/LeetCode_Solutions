class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        
        max_ = max(a,b,c)
        total = a+b+c
        
        if total >= max_*2:
            return total//2
        else:
            return total-max_