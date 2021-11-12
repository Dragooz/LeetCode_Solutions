#Reference: https://leetcode.com/problems/people-whose-list-of-favorite-companies-is-not-a-subset-of-another-list/discuss/636512/Python3-Easy-Solution

class Solution:
    def peopleIndexes(self, FV: List[List[str]]) -> List[int]:
        
        d = {i:set(fv) for i, fv in enumerate(FV)}
        ans = []
        
        for i in range(len(FV)):
            
            not_sub = True
            
            for j in range(len(FV)):
                if i == j:
                    continue
                    
                if not d[i] - d[j]: #this means d[i] is subset of d[j]
                    not_sub = False
                    
            if not_sub:
                ans.append(i)
        
        return ans
                
            
            