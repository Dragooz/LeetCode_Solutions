#Reference: https://leetcode.com/problems/maximum-sum-obtained-of-any-permutation/discuss/854206/JavaC%2B%2BPython-Sweep-Line

class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        
        n = len(nums)
        
        count = [0] * (n + 1)
        
        for i, j in requests:
            count[i] += 1
            count[j+1] -= 1
            
        for i in range(1, n):
            count[i] += count[i-1]
        
        print(count)
        ans = 0 
        for num, freq in zip(sorted(nums, reverse=True), sorted(count, reverse=True)):
            ans += num * freq
            
        return ans % (10**9+7)