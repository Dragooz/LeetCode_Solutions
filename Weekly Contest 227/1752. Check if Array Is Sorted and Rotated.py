class Solution:
    def check(self, nums: List[int]) -> bool:
        
        new_num = nums
        
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                new_num = nums[i+1:] + nums[:i+1]
                break
        
                
        return new_num == sorted(nums)
        