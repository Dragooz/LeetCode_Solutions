class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        
        ans = 0
        while piles:
            piles.pop(-1)
            ans += piles.pop(-1)
            piles.pop(0)
            
        return ans