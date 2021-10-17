#Reference: https://leetcode.com/problems/the-time-when-the-network-becomes-idle/discuss/1524169/Python-Clean-BFS-Lots-Of-Comments-Easy-To-Follow

class Solution:
    def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:
        
        adjlist = defaultdict(list)
        
        for u, v in edges:
            adjlist[u].append(v)
            adjlist[v].append(u)
            
            
        shortest = {}
        seen = set()
        queue = [(0,0)]        
        while queue:
            cur_pos, cur_dist = queue.pop(0)
            
            if cur_pos in seen:
                continue
            
            seen.add(cur_pos)
            shortest[cur_pos] = cur_dist
            
            for nei in adjlist[cur_pos]:
                queue.append((nei, cur_dist +1))
        
        ans =0
        for i in range(1, len(patience)):
            
            resend_interval = patience[i]
            
            shut_off = shortest[i] * 2
            
            last_resend = ((shut_off-1) // (resend_interval)) * resend_interval
            
            ans = max(ans, last_resend + shut_off) #the last still need to go through the cycles.
            
        return ans +1 #First second is idle
            
            
            
            
            