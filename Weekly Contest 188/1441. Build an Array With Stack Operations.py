class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        
        pp = ['Push', 'Pop']
        
        ans = []
        cur = 0
        for i in range(1, max(target)+1):
            
            ans.append(pp[0])
            
            if i != target[cur]:
                ans.append(pp[1])
            else:
                cur+=1
                
        return ans