import numpy as np

class Solution(object):
    def eliminateMaximum(self, dist, speed):
        """
        :type dist: List[int]
        :type speed: List[int]
        :rtype: int
        """
        dist = np.array(dist).astype(float)
        speed = np.array(speed).astype(float)
        
        
        new_array = sorted(np.ceil(dist/speed)) #so here minimum is 1

        for index, value in enumerate(new_array):
            if (value-index) == 0:
                return index
            
        return len(dist)
            