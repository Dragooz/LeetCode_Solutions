class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        
        if n == 0:
            return 0
        
        nums = [0] * (n+1)
        nums[1] = 1
        
        for i in range((n+1)//2):
            nums[i*2] = nums[i]
            nums[i*2 + 1] = nums[i] + nums[i+1] 
        
        return max(nums)