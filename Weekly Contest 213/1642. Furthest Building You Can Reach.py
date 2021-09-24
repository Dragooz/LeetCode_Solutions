#Reference: https://leetcode.com/problems/furthest-building-you-can-reach/discuss/918515/JavaC%2B%2BPython-Priority-Queue

from heapq import *

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        
        n = len(heights)
        
        heap = []

        for i in range(n-1):
            
            diff = heights[i+1] - heights[i]
            if diff >0:
                heappush(heap, diff)
                
            if len(heap) > ladders:
                bricks -= heappop(heap)
                
            if bricks <0:
                return i
                
        return len(heights) -1 #all can reach
                    
                    
        