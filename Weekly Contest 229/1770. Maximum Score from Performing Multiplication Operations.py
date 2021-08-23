#Reference: https://leetcode.com/problems/maximum-score-from-performing-multiplication-operations/discuss/1075469/JavaC%2B%2BPython-3-Top-Down-DP-O(m2)-Clean-and-Concise by hiepit

from functools import lru_cache

class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        #dp
        
        n = len(nums)
        m = len(multipliers)
        
        @lru_cache(2000)
        def dp(l, i):
            if i == m: return 0
            
            left = dp(l+1, i+1) + multipliers[i] * nums[l]
            right = dp(l, i+1) + multipliers[i] * nums[n-1 -(i-l)]
            
            return max(left, right)
        
        return dp(0, 0)