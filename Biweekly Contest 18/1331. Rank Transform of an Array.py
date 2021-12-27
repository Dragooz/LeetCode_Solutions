class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        
        unique = sorted(list(set(arr)))
        
        dict_ = {i:index+1 for index, i in enumerate(unique)}
        
        return [dict_[i] for i in arr]
        
        
        
        
        
        