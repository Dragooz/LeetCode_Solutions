class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        
        arr.sort()
        median = arr[(len(arr)-1) // 2]
        
        arr = sorted([(abs(i-median), i) for i in arr], key= lambda x: [x[0], x[1]] ,reverse=True)
        return [arr[i][1] for i in range(k)]
        
        