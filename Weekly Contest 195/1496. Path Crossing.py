class Solution:
    def isPathCrossing(self, path: str) -> bool:
        
        seen = {(0,0)}
        cur = (0,0)
        for char in path:
            if char == 'N':
                cur = (cur[0], cur[1] +1)
            elif char == 'S':
                cur = (cur[0], cur[1] -1)
            elif char == 'E':
                cur = (cur[0]-1, cur[1])
            else:
                cur = (cur[0]+1, cur[1])

            if cur in seen:
                return True
            else:
                seen.add(cur)
                
            print(seen)
                
        return False