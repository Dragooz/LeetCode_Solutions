#Reference: https://leetcode.com/problems/minimum-speed-to-arrive-on-time/discuss/1224638/Clean-Python-3-binary-search by lenchen1112

import math

class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        #main idea:
        #dist length-1 is basically the minimum hour need to reach.
        #last dist is the key to the float.
        #if sum(ceil(dist/speed)) > hour: increment speed.
        
        dl = len(dist)
        
        if (dl-1) > hour:
            return -1
        
        low = 0 #minimum speed is 1, the most possible is (0, 1), so return high is correct
        high = 10**7 #maximum speed #at most 2 digit behind
        
        while(low+1 < high):
            mid = low + (high - low) //2
            divided = sum([math.ceil(d/mid) for d in dist[:-1]]) + dist[-1]/mid
            # print(divided)
            # print(low, mid, high)
            
            if divided <= hour: #hour needed, hour allowed, this means the solution is ok, speed need to be decrease.
                high = mid 
                # print('needed < allowed')
                # print(divided)
                # print(low, mid, high)
                
            elif divided > hour: #hour needed, hour allowed, solution not valid, speed need to be increase
                low = mid
                # print('needed > allowed')
                # print(divided)
                # print(low, mid, high)
        
        # print('final:')
        # print(divided)
        # print(low, mid, high)
        divided = sum([math.ceil(d/high) for d in dist[:-1]]) + dist[-1]/high #reconfirm using high
        return high if (divided <= hour) else -1
 