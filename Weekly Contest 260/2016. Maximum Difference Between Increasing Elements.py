class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        
        ans = 0
        n = len(nums)
        
        for i in range(n):
            for j in range(i+1, n):
                ans = max(ans, nums[j] - nums[i])
                
        if ans == 0:
            return -1
        else:
            return ans