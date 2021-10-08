#Reference: https://leetcode.com/problems/min-cost-to-connect-all-points/discuss/843995/Python-3-or-Min-Spanning-Tree-or-Prim's-Algorithm

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        #prim's algo
        
        def dist(x, y):
            return abs(x[0] - y[0]) + abs(x[1] - y[1])
        
        ans = 0
        n = len(points)
        
        seen = set()
        vertices = [(0, (0, 0))] #dist, start vertices, next vertices
        
        while len(seen) < n:
            
            w, (u, v) = heappop(vertices)
            
            if v in seen: continue
            
            ans += w
            seen.add(v)
            
            for j in range(n):
                if j not in seen:
                    heappush(vertices, [dist(points[j], points[v]), (v, j)])# keep pushing possible, and it will pick only minimum
                    
        return ans