from collections import defaultdict

class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        prefix_sum = [0] * (n+1)
        prefix_sum[1] = nums[0]
        
        for i in range(1, n):
            prefix_sum[i+1] = prefix_sum[i] + nums[i]
            
        dp = defaultdict()
        ans = []
        
        for i, num in enumerate(nums):
            if dp.get(num, -1) == -1:
                dp[num] = (prefix_sum[-1] - prefix_sum[i] - num*(n-i)) + ((num*i) - prefix_sum[i])
                
            ans.append(dp[num])
            
        return ans
        