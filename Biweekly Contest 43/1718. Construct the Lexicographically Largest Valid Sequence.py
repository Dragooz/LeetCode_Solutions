#Reference: https://leetcode.com/problems/construct-the-lexicographically-largest-valid-sequence/discuss/1008948/Python-Greedy%2BBacktracking-or-Well-Explained-or-Comments

class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        
        ans = [0] * (n*2 -1)
        
        seen = set()

        def dfs(idx):
            if (len(seen)==n): return ans #all used.

            if (ans[idx]): return dfs(idx+1) #already has number    

            for x in range(n,0,-1):
                if (x not in seen): #not used yet
                    sec = idx+x
                    if (x==1): sec = idx #if '1' then only can insert once

                    if (sec < len(ans) and ans[idx]==0 and ans[sec]==0): #in the condition
                        ans[idx], ans[sec] = x,x
                        seen.add(x)
                        a = dfs(idx+1) #proceed.
                        if a: return a #if it return stuff, means all seen is there. return the answer
                        seen.remove(x) #else, backtrack.
                        ans[idx] , ans[sec] = 0,0

        return dfs(0)
                