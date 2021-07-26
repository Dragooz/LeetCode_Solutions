from itertools import combinations

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        #XOR of the char against 0
        #XOR of each combination
        
        ans = sum(nums)
        
        for i in range(2, len(nums)+1):
            comb = combinations(nums, i)
            for com in comb:#each comb
                temp = 0
                for c in com:
                    temp = temp ^ c
                
                ans += temp
            
        return ans
        