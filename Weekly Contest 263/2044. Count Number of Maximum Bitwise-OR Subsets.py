#Reference: https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/discuss/1525309/JavaC%2B%2BPython-DP-solution

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        n = len(nums)
        
        dp = Counter([0])
        
        for num in nums:
            dp_ = copy.deepcopy(dp)
            for k, v in dp_.items():
                dp[k | num] += v
                
        return dp[max(dp)]
    
                    