for i in range(m):
    for j in range(n):
        
        if land[i][j]:
            
            min_i, min_j = i, j
            max_i, max_j = i, j
            
            stack = [(i, j)]
            land[i][j] = 0
            
            while stack:
                i, j = stack.pop()
                
                for ii, jj in (i-1, j), (i, j-1), (i, j+1), (i+1, j):
                    if 0<=ii<m and 0<=jj<n and land[ii][jj]:
                        stack.append((ii,jj))
                        land[ii][jj] = 0
                        max_i = max(max_i, ii)
                        max_j = max(max_j, jj)
                        
            ans.append([min_i, min_j, max_i, max_j])
            
#--------------------------------------------------------------------------------------

class Solution:
    def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:
        
        seen = set()
        operations = [add, sub, xor]
        queue = [start]
        ans = 0
        
        while queue:
            
            for _ in range(len(queue)):
                val = queue.pop(0)
                
                if val == goal:
                    return ans

                if 0 <= val <= 1000:
                    for num in nums:
                        for op in operations:
                            res = op(val, num)

                            if res not in seen:
                                seen.add(res)
                                queue.append(res)

            ans+=1
            
        return -1
                        