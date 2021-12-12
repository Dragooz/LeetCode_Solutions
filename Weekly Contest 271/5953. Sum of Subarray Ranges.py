class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)-1):
            
            min_ = nums[i]
            max_ = nums[i]
            
            for j in range(i+1, len(nums)):
                
                min_ = min(min_, nums[j])
                max_ = max(max_, nums[j])
                
                ans+= max_ - min_
                
        return ans