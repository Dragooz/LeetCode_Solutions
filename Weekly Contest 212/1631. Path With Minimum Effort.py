#Reference: https://leetcode.com/problems/path-with-minimum-effort/discuss/909017/JavaPython-Dijikstra-Binary-search-Clean-and-Concise

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        
        n, m = len(heights), len(heights[0])
        
        dist = [ [math.inf] * m for _ in range(n) ]
        
        min_heap = [(0,0,0)] #dist, row, col
        DIR = [0, 1, 0, -1, 0]
        
        while min_heap:
            d, r, c = heappop(min_heap)
            
            if d > dist[r][c]: #if bigger, then ignore
                continue
                
            if r+1 == n and c+1 == m:
                return d
            
            for i in range(4):
                nr, nc = r+DIR[i], c+DIR[i+1]
                if 0 <= nr < n and 0 <= nc < m:
                    new_dist = max(d, abs(heights[nr][nc] - heights[r][c])) #max here as we need to track the maximum diff
                    if dist[nr][nc] > new_dist:
                        dist[nr][nc] = new_dist
                        heappush(min_heap, (new_dist, nr, nc))
                        
        
            