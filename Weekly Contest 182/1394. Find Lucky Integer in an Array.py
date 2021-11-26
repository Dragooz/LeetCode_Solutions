class Solution:
    def findLucky(self, arr: List[int]) -> int:
        
        c = sorted(dict(Counter(arr)).items(), key=lambda kv: kv[0], reverse=True)
        print(c)
        
        for key, val in c:
            if key == val:
                return key
            
        return -1