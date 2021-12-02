#Reference: https://leetcode.com/problems/time-needed-to-inform-all-employees/discuss/532560/JavaC%2B%2BPython-DFS

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        
        children = [[] for i in range (n)]
        
        for i, m  in enumerate(manager):
            if m >= 0:
                children[m].append(i)
                
        def dfs(i):
            max_ = max([dfs(j) for j in children[i]] or [0]) #get max inform time
            return max_ + informTime[i]
        
        return dfs(headID)