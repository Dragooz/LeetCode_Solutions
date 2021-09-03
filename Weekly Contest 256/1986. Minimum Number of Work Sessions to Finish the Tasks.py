#First attempt: Wrong answer

from itertools import combinations
class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        
        tasks.sort()
        
        ans = 0
        i=1
        
        while tasks and i<=len(tasks): #get rid of all possible combination that results in sessionTime
            comb = combinations(tasks, i)
 
            for pairs in list(comb):
                if sum(pairs) == sessionTime:
                    for val in pairs:
                        tasks.remove(val)
                    
                    i=1
                    ans+=1
                    break
            
            i+=1
            
        while tasks: #for the remaining that is not perfect, selecting from the greatest to lowest
            quota = sessionTime
            ans+=1
            
            while quota > 0:
                i = bisect.bisect_right(tasks, quota) #right most item greater than quota
                if tasks and tasks[i-1] <= quota:
                    quota -= tasks.pop(i-1)
                else:
                    quota = -1
        
        return ans
    
#Second Attempt: Reference: https://leetcode.com/problems/minimum-number-of-work-sessions-to-finish-the-tasks/discuss/1436811/C%2B%2BJavaPython-From-Straightforward-to-Optimized-Bitmask-DP-O(2n-*-n)-Clean-and-Concise

from itertools import combinations
from functools import lru_cache
class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        #mask --> series of '1's indicating which task must be done
        #final = all '0's in mask
        
        n = len(tasks)
        
        def clear_bit(mask, i): #remove '1' in mask indicating task finished
            return ~(1<<i) & mask
        
        @lru_cache(None)
        def dp(mask, rt):
            if mask == 0: return 0
            ans = n
            for i in range(n):
                if mask>>i & 1: #task available
                    new_mask = clear_bit(mask, i)
                    if tasks[i] <= rt:
                        ans = min(ans, dp(new_mask, rt-tasks[i]))
                    else:
                        ans = min(ans, dp(new_mask, sessionTime-tasks[i]) +1)
                              
            return ans
                              
        return dp((1<<n) -1, 0)
    
