class Solution(object):
    def rotateGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        
        w = len(grid[0])
        h = len(grid)
        
        #flatten
        top = grid[0][:]
        right = [row [-1] for row in grid[1:-1]]
        bottom = grid[-1][:][::-1] #flip to correct seq
        left = [row [0] for row in grid[1:-1]][::-1] #flip to correct seq
        
        sequence = top + right + bottom + left
        
        #rotate
        num_r = k % len(sequence)
        print(num_r)
        sequence_a = sequence[num_r:] + sequence[0:num_r]
        
        #stripped
        stripped = [ row[1:-1] for row in grid[1:-1] ]

        if stripped != [] and stripped[0] != []: #ensure it is not empty
            stripped = self.rotateGrid(stripped, k)

        #reconstruct
        top = sequence_a[:w]
        right = sequence_a[w:w+h-2]
        bottom = sequence_a[w+h-2:(2*w)+h-2][::-1] #flip to correct seq
        left = sequence_a[(2*w)+h-2:][::-1] #flip to correct seq
        
        
        grid_middle = [[a] + b + [c] for a,b,c in zip(left, stripped, right)] #so that they same with stripped's format
        grid = [top] + grid_middle + [bottom] #so that they same with grid_middle's format
        
        return grid
        
        
        