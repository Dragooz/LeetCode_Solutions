class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        
        lr = len(rolls)
        sr = sum(rolls)
        
        final = (lr + n) * mean
        
        diff = final - sr
        
        ans = []
        if diff <= (n*6):
            diff -= (1*n)
            if diff < 0:
                return ans
            
            ans = [1] * n
            
            i = 0
            while diff>=5:
                ans[i] += 5
                diff -= 5
                i+=1
            if diff != 0:
                ans[i] += diff
            
        return ans
                
        
        