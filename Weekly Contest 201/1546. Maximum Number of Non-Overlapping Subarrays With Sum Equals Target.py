#Reference: https://leetcode.com/problems/maximum-number-of-non-overlapping-subarrays-with-sum-equals-target/discuss/780887/Java-Detailed-Explanation-DPMapPrefix-O(N)

class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        
        prefix = [0] + [i for i in accumulate(nums)]
        
        ans, seen = 0, set()
        for num in prefix:
            if (num-target) in seen:
                ans +=1
                seen = {num}
            else:
                seen.add(num)
            
        return ans