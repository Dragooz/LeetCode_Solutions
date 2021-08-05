class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        
        i=0
        while i <len(nums)-1:
            if nums[i+1] <= nums[i]:
                ans += abs(nums[i+1] - nums[i])+1
                nums[i+1] += abs(nums[i+1] - nums[i])+1
                
            i+=1
            
        return ans