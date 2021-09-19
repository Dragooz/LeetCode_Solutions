class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        
        ans = 0
        
        for a in operations:
            if '+' in a:
                ans+=1
            else:
                ans-=1
                
        return ans