#Reference: https://leetcode.com/problems/last-day-where-you-can-still-cross/discuss/1403907/C%2B%2BPython-Binary-Search-and-BFS-Clean-and-Concise by hiepit

class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        #breath first search (find valid path) > binary search (find valid day)
        direction = [[1,0], [0,1], [0,-1], [-1,0]]
        
        def can_walk_day(day):
            map_ = [[0]*col for _ in range(row)]
            for r, c in cells[:day]:
                map_[r-1][c-1] = 1
                
            bfs = []
            
            for i in range(col):
                if map_[0][i] != 1:
                    bfs.append([0, i]) #loop through all col of first row
                    map_[0][i] = 1 #visited
                    
            while bfs:
                r, c = bfs.pop(0)
                
                if r == row -1: #reach
                    return True

                for fd, sd in direction:
                    
                    nr, nc = r+fd, c+sd
                    if nr==row or nc==col or nr<0 or nc< 0 or map_[nr][nc] == 1: 
                        continue
                    else:
                        map_[nr][nc] = 1
                        bfs.append([nr, nc])

            return False
        
        #binary search
        
        low, high = 1, len(cells)

        ans = 0
        while low <= high:
            mid = (low+high)//2
            
            if can_walk_day(mid): #means it can be more day
                ans = mid #the answer so far
                low = mid +1
            else:
                high = mid -1 #means it need be less day
            
        return ans