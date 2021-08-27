#Reference from https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/discuss/1052527/JavaC%2B%2BPython-O(1)-Space by lee215
class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        ans = 0
        
        #loop through and get the max of positive
        temp = 0
        for num in nums:
            temp += num
            
            temp = max(0, temp)
            ans = max(ans, temp)
            
        #loop through and get the min of positive
        
        temp = 0
        nums = [-i for i in nums]
        
        for num in nums:
            temp+= num
            temp = max(0, temp)
            ans = max(ans, temp)
            
        return ans

# OR

from itertools import accumulate

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        
        return max(accumulate(nums, operator.add, initial=0)) - min(accumulate(nums, operator.add, initial=0))

            