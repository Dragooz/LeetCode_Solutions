#Reference:
#https://leetcode.com/problems/get-biggest-three-rhombus-sums-in-a-grid/discuss/1238730/Python-dp-O(mn*min(mn))-solution-explained by DBabichev

import heapq

class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        
        #main idea:
        #use heap to store biggest 3
        #use dynamic programming, prefix sum idea
        #four direction, add up.
        
        m = len(grid)
        n = len(grid[0])
        
        heap = []
        
        def update(heap, num): #update heap
            
            if num not in heap:#push
                heapq.heappush(heap, num)
            
            if len(heap) > 3:
                heapq.heappop(heap)
            return heap
        
        for i in chain(*grid): #get all possible biggest 1 combination
            update(heap, i) 
        
        @lru_cache(None)
        def dp(i, j, dr): #i, j and direction
            if not 0<=i<n or not 0<=j<m:
                return 0 #either i or j out the boundaries, return 0
            return dp(i-1, j+dr, dr) + grid[j][i]
        
        cube_size = range(1, (min(m, n)+1)//2 ) 
        
        for q in cube_size: 
            for i in range(q, n-q):
                for j in range(q,m-q):
                    # print('q:', q)
                    # print('i:', i)
                    # print('j:', j)
                    
                    #dr=-1, means direction from upper left to lower right, get the sum of right side, index match exactly the cube
                    p1 = dp(i + q, j, -1) - dp(i, j - q, -1) 
                    
                    # print('dp(i + q, j, -1):', dp(i + q, j, -1))
                    # print('dp(i, j - q, -1):', dp(i, j - q, -1))
                    # print('p1:', p1)
                    
                    #dr=-1, means direction from upper left to lower right, get the sum of left side, index above 1 from the cube.
                    p2 = dp(i - 1, j + q - 1, -1) - dp(i - q - 1, j - 1, -1)
                    # print('dp(i - 1, j + q - 1, -1):', dp(i - 1, j + q - 1, -1))
                    # print('dp(i - q - 1, j - 1, -1):', dp(i - q - 1, j - 1, -1))
                    # print('p2:', p2)
                    
                    #dr=1, means direction from upper right to lower left, get the sum of left side, index match exactly the cube.
                    p3 = dp(i, j - q, 1) - dp(i - q, j, 1) #dr = 1, means direction from upper right, to lower left
                    # print('dp(i, j - q, 1):', dp(i, j - q, 1))
                    # print('dp(i - q, j, 1):', dp(i - q, j, 1))
                    # print('p3:', p3)
                    
                    #dr=1, means direction from upper right to lower left, get the sum of right side, index below 1 from the cube.
                    p4 = dp(i + q - 1, j + 1, 1) - dp(i - 1, j + q + 1, 1)
                    # print('dp(i + q - 1, j + 1, 1):', dp(i + q - 1, j + 1, 1))
                    # print('dp(i - 1, j + q + 1, 1):', dp(i - 1, j + q + 1, 1))
                    # print('p4:', p4)
                    
                    update(heap, p1+p2+p3+p4)
            
        return sorted(heap)[::-1]
        