import math

class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        
        #main idea:
        #1. Add a zero as initial step at the beginning of the array
        #2. Get the distance array between each element in the array
        #3. if dist >= the distance array element, the rung should be zero
        #   elif distance array element > dist, return ceil(dae/dist) -1
        
        if rungs[0] != 0: #1.
            rungs.insert(0, 0)
        
        dist_array = [b-a for a, b in zip(rungs[:-1], rungs[1:])] #2.
        
        ans = 0
        for da in dist_array:
            if dist >= da:
                pass
            elif da>dist:
                ans += math.ceil(da/dist) -1
                
        return ans