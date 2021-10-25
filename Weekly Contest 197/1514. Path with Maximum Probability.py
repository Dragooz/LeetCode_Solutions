#Reference: https://leetcode.com/problems/path-with-maximum-probability/discuss/731767/JavaPython-3-2-codes%3A-Bellman-Ford-and-Dijkstra's-algorithm-w-brief-explanation-and-analysis.

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        
        
        p = [0.0] * n 
        graph = defaultdict(list)
        
        for (u, v), prob in zip(edges, succProb):
            graph[u].append([v, prob])
            graph[v].append([u, prob])
            
        p[start] = 1
        
        heap = [(-p[start], start)]
        
        while heap:
            prob, cur = heapq.heappop(heap)
            
            if cur == end:
                return -prob
            
            for neigh, probb in graph.get(cur, []):
                if -prob*probb > p[neigh]: #negative here turn it back to positive
                    p[neigh] = -prob*probb
                    heappush(heap, (-p[neigh], neigh))
        return 0.0
        