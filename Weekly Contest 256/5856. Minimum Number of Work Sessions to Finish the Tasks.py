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
    
