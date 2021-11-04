class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        
        prefix = {0: -1}
        
        min_length = [math.inf] * len(arr)
        
        ans = min_ = math.inf
        
        for index, cur in enumerate(accumulate(arr)):
            if cur - target in prefix:
                end = prefix[cur-target]
                 
                ans = min(ans, index-end+min_length[end]) #min_length at the last always the best
                min_ = min(min_, index-end)
                
            min_length[index] = min_
            prefix[cur] = index
            
        return -1 if ans == math.inf else ans
        
                
        