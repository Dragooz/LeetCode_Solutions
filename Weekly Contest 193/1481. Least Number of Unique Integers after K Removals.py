class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        
        count = Counter(arr)
        
        ans = 0
        
        for key, val in count.most_common()[::-1]:
            if k >= val:
                k -= val
            else:
                ans+=1
        
        return ans
            