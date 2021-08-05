from collections import defaultdict

class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        k = []
        
        memo = defaultdict()
        memo[0] = nums[0]
        for i in range(1, len(nums)):
            memo[i] = memo[i-1]^nums[i]
        
        for j in range(len(nums)-1, -1, -1):
            
            #flip 
            k.append(memo[j] ^ ((2**maximumBit)-1))
            
        return k
