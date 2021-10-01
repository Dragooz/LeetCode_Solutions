import numpy as np

class Solution:
    def specialArray(self, nums: List[int]) -> int:
        
        nums = np.array(nums)
        
        for i in range(1, 101):
            ans = sum(nums>=i)
            if i == ans:
                return i
            
        return -1