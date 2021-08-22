#first try: TLE

from functools import lru_cache

class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        
        n = len(mat)
        m = len(mat[0])
        
        @lru_cache(None)
        def dp(index, t_weight):
            
            if index == n:
                return abs(target-t_weight)
            
            if t_weight == target:
                list_ = [min(mat[index])]
            else:
                list_ = mat[index]
                
            min_ = sys.maxsize
            
            for l in list_:
                
                if target+min_ > t_weight+ l:
                    min_ = min(min_, dp(index+1, t_weight+l))

            return min_
            
        return dp(0, 0)

#Second try: 
#Reference: https://leetcode.com/problems/minimize-the-difference-between-target-and-chosen-elements/discuss/1418602/Python-4-lines-solution-explained by DBabichev

from functools import lru_cache

class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        
        possible_min = sum(min(i) for i in mat)
        
        if possible_min > target:
            return abs(target- possible_min)
        
        nums = {0}
        
        for row in mat:
            nums = {x+i for i in nums for x in row if x+i <= 2*target - possible_min}
        
        return min(abs(target-i) for i in nums)