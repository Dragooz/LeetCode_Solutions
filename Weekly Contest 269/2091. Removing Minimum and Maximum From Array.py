class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        
        min_, min_i = math.inf, 0
        max_, max_i = -math.inf, 0
        
        n = len(nums)
        
        for i in range(n):
            
            if min_ > nums[i]:
                min_ = nums[i]
                min_i = i
            
            if max_ < nums[i]:
                max_ = nums[i]
                max_i = i
            
        max_left = max(min_i+1, max_i+1) #only remove left 
        max_right = max(n-min_i, n-max_i) #only remove right
        max_left_right = min(min_i+1, n-min_i) + min(max_i+1, n-max_i) #left and right
        
        return min(max_left, max_right, max_left_right)
        
        