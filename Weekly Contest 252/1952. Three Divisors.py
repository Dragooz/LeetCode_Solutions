class Solution:
    def isThree(self, n: int) -> bool:
        ans=2
        for i in range(2, (n//2)+1):
            if n % i == 0:
                ans+=1
        
        return ans==3