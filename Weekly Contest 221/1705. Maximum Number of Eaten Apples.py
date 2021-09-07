#Reference: https://leetcode.com/problems/maximum-number-of-eaten-apples/discuss/988209/Easy-Python-Solution-with-Explanation-ACCEPTED

from heapq import *

class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        
        i = 0
        ans = 0
        q =[]
        
        while i<len(apples) or q:

            if i< len(apples) and apples[i]>0:
                heappush(q, [days[i]+i, apples[i]])
            
            while q and(q[0][0] <= i or q[0][1] <= 0): #rotten or out of apples
                heappop(q)
                
            if q: #if there's apple not rot
                q[0][1] -= 1 #eat 1 apple
                ans +=1 #record
                
            i+=1
            
        return ans