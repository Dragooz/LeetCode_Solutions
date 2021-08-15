import random
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        def check(nums):
            for i in range(1, len(nums)-1):
                if (nums[i-1] + nums[i+1]) / 2  == nums[i]:
                    return False
            
            return True
        
        while not check(nums):
            random.shuffle(nums)
            
        return nums