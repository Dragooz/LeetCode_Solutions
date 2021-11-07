#Reference: https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/discuss/661774/Python3-Easy-Short-DFS

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        
        graph = defaultdict(list)
        self.ans = 0
        
        
        for u, v in connections:
            graph[u].append((v, 1)) #imagine is 0 to 1 (u to v), then it cost 1
            graph[v].append((u, 0))
            
        queue = [0]
        visited = {0}
        ans = 0
        
        while queue:
            city = queue.pop(0)
            
            for neigh, cost in graph[city]:
                if neigh in visited:
                    continue
                visited.add(neigh)
                ans += cost
                queue.append(neigh)
                
        return ans
                
            
        