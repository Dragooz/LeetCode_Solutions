class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        
        if k == 0:
            return True
        
        i = 0
        while i<len(nums):
            if nums[i] == 1:
                if 1 in nums[i+1: i+1+k]:
                    return False
                else:
                    i+= k - 1
        
            i+=1
            
        return True