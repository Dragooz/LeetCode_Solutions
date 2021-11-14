#Reference: https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/discuss/623673/Concise-explanation-with-a-Picture-for-Visualization

class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        
        graph = defaultdict(list)
        
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        seen = set()
        
        def dfs(node):
            if node in seen:
                return 0
            
            seen.add(node)
            
            seconds = 0
            
            for child in graph[node]:
                seconds += dfs(child)
                
            if seconds > 0 : return seconds +2
            
            return 2 if hasApple[node] else 0
        
        return max(dfs(0)-2, 0) 