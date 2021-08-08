import math
from heapq import *
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        
        def round_up (val):
            return math.floor(val/2) #handling negative, so floor
        
        piles = [-p for p in piles]
        
        heapify(piles)
        
        for _ in range(k):
            temp = heappop(piles)
            heappush(piles, round_up(temp))
            
        return -sum(piles)