#First Attempt: TLE

from collections import defaultdict
from heapq import *
from functools import lru_cache

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        
        @lru_cache(None) 
        def dp(cur, quota): #depth first search
            
            if cur == 0 and quota == 0:
                return 1
            
            if quota<=0 :
                return 0
            
            valid = 0
            
            for neigh, dist in graphs[cur]:
                valid += dp(neigh, quota-dist)
                
                
            return valid
        
        #build graphs
        graphs = defaultdict(list)
        
        for u,v,w in roads:
            graphs[u].append((v, w))
            graphs[v].append((u, w))
            
        #find shortest dist from start(1) to end(n)
        
        shortest_dist = [sys.maxsize]* n
        shortest_dist[n-1] = 0
        visited = set()
        pq = [[0, n-1]] #[dist, node]
        
        #get nodes with shortest dist to the destination
        while pq:
            d, cur = heappop(pq)
            visited.add(cur)
            
            for neigh, dist in graphs[cur]:
                if neigh not in visited:
                    total_dist = d + dist 
                    if total_dist < shortest_dist[neigh]: #if its shorter
                        heappush(pq, [total_dist, neigh]) #next node
                        shortest_dist[neigh] = total_dist #update

        return dp(n-1, shortest_dist[0]) % (10**9 +7)
        
        
#Second attempt: 
#Reference from: https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/discuss/1417573/python-Almost-Dijktra-explained by DBabichev

from collections import defaultdict
from heapq import *
from functools import lru_cache

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        
        #build graphs
        graphs = defaultdict(list)
        
        for u,v,w in roads:
            graphs[u].append((v, w))
            graphs[v].append((u, w))
            
        #find shortest dist from start(1) to end(n)
        
        shortest_dist = [sys.maxsize]* n
        shortest_dist[0] = 0
        
        #counter
        count = [0] * n
        count[0] = 1

        pq = [[0, 0]] #[dist, node]
        
        #get nodes with shortest dist to the destination
        while pq:
            d, cur = heappop(pq)
            
            if cur == n-1: return count[cur] % (10**9 +7)
            
            for neigh, dist in graphs[cur]:
                
                total_dist = shortest_dist[cur] + dist
                
                if total_dist == shortest_dist[neigh]: #found a path with same dist
                    count[neigh] += count[cur]
                    
                elif total_dist < shortest_dist[neigh]: #found a better path
                    
                    heappush(pq, [total_dist, neigh]) #next node
                    shortest_dist[neigh] = total_dist #update
                    count[neigh] = count[cur]
        
        
        