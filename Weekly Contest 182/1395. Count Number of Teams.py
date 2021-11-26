#Reference: https://leetcode.com/problems/count-number-of-teams/discuss/565479/python-greater97.98-simple-logic-and-very-detailed-explanation

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        
        ans= 0
        for i, r in enumerate(rating):
            llc, lgc, rlc, rgc = 0, 0, 0, 0 #left less counter, left great counter, right less counter, right great counter
            
            for rj in rating[i+1:]:
                if rj < r:
                    rlc+=1
                
                if r < rj:
                    rgc+=1
                    
            for rk in rating[:i]:
                if rk < r:
                    llc+=1
                
                if r < rk:
                    lgc+=1
                                 
            ans += llc * rgc
            ans += lgc * rlc
            
        return ans
            
            
            