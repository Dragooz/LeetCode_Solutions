class Solution:
    def nextBeautifulNumber(self, n: int) -> int:

        for i in range(n+1, (10**6) +1):
            counter = Counter(str(i))
            
            if all(int(key)==int(val) for key, val in counter.most_common()):
                return i
            
        return 1224444
        
                
        
        
        
            