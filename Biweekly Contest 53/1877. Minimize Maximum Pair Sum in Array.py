class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        
        pair = []
        nums.sort()
        
        while nums:
            min_, max_ = nums.pop(0) , nums.pop(-1)

            pair.append(min_+max_)
            
        return max(pair)