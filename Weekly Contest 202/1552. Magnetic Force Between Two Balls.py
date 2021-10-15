#Reference: https://leetcode.com/problems/magnetic-force-between-two-balls/discuss/794070/PythonC%2B%2B-Binary-search-solution-with-explanation-and-similar-questions

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        
        n = len(position)
        position.sort()

        def count(d): #take in distance as input
            ans, cur_pos = 1, position[0] #ans means how many balls can be put to achieve d.
            
            for i in range(1, n):
                if position[i] - cur_pos >= d: 
                    ans+=1
                    cur_pos = position[i]
                    
            return ans #return the balls put
        
        
        l, r = 0, position[-1] - position[0]
        
        while l<r:
            mid = r - (r-l)//2
            
            if count(mid) >= m: #too many balls can be put
                l = mid
            else: #too less to put
                r = mid-1
            
        return l
            
        