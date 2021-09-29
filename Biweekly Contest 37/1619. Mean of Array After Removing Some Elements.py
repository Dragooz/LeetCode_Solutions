class Solution:
    def trimMean(self, arr: List[int]) -> float:
        
        arr.sort()
        
        n = len(arr)
        
        remove = n//20
        
        return sum(arr[remove:n-remove]) / (n-(remove*2))