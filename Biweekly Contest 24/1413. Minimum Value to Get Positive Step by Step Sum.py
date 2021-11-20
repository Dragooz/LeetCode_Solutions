class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        
        prefix_sum = list(accumulate(nums))
        
        min_ = min(prefix_sum)
        
        if min_ >= 0:
            return 1
        else:
            return abs(min_) +1