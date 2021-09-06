#Reference: https://leetcode.com/problems/ways-to-split-array-into-three-subarrays/discuss/999257/C%2B%2BJavaPython-O(n)-with-picture

from itertools import accumulate

class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        
        n = len(nums)
        ans, j, k = 0, 0, 0
        mod = (10**9) +7
        
        prefix_sum = list(accumulate(nums)) 
        
        for i in range(n-2):
            
            while j <= i or (j < n-1 and prefix_sum[i] * 2 > prefix_sum[j]): #find min j position
                j+=1
                
            while k < j or (k < n-1 and prefix_sum[k] - prefix_sum[i] <= prefix_sum[-1] - prefix_sum[k]): #find max k position
                k+=1
                
            ans = (ans + k-j) % mod
            
        return ans
        
        