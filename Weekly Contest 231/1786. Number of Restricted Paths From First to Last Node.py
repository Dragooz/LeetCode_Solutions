#Reference from https://www.youtube.com/watch?v=YmufKoAmthE by Happy Coding

from collections import defaultdict
from heapq import *
from functools import lru_cache

class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        
        @lru_cache(None)          
        def dp(cur): #depth first search
            if cur == n:
                return 1
            
            valid = 0
            
            for neigh, _ in graphs[cur]:
                if shortest_dist[cur] > shortest_dist[neigh]:
                    valid += dp(neigh)
                
            return valid
        
        #build graphs
        graphs = defaultdict(list)
        
        for u,v,w in edges:
            graphs[u].append((v,w))
            graphs[v].append((u,w))
            
        #find shortest dist from start(1) to end(n) 
        #dijkstra algo that focus on start(1) to end(n)
        
        shortest_dist = [sys.maxsize] * (n+1) #track the shortest distance of start(1) to the diff nodes.
        shortest_dist[n] = 0 #the destination node one gonna be 0
        visited = set() #track visited nodes
        pq = [[0, n]] #priority queue, [dist, node]
        
        #after this while loop, all nodes will have the shortest distance to the end.
        while pq:
            d, cur = heappop(pq) #we loop from the ends
            visited.add(cur) #visited the node
            
            for neigh, dist in graphs[cur]: #find all neighbours of the current nodes
                if neigh not in visited: #not yet visit
                    total_dist = d + dist #current weight + the progress weight
                    if total_dist < shortest_dist[neigh]: #if the visited nodes has higher than the current
                        heappush(pq, [total_dist, neigh]) #push to queue so that the neigh node will be explore
                        shortest_dist[neigh] = total_dist #update
                        
        return dp(1) % (10**9 +7)
        
        