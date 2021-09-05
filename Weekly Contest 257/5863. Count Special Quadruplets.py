from itertools import combinations
 

class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        
        ans = 0
        comb = combinations(nums, 4)
        # Print the obtained combinations
        for i in list(comb):
            if i[0] + i[1] + i[2] == i[3]:
                ans +=1
                
        return ans