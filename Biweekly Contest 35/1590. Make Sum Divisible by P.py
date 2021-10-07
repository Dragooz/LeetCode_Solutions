#Reference: https://leetcode.com/problems/make-sum-divisible-by-p/discuss/854197/JavaC%2B%2BPython-Prefix-Sum

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
    
        total = sum(nums)
        remainder = total % p

        dp = {0: -1}
        
        cur = 0
        ans = n = len(nums)
        
        for i, num in enumerate(nums):
            cur = (cur + num) % p
            dp[cur] = i
            if (cur - remainder)%p in dp:
                ans = min(ans, i-dp[(cur-remainder)%p])
            
        return ans if ans<n else -1
                
            