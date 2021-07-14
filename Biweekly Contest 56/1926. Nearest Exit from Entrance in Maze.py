
#DFS approach but failed (time limit)
'''
https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/discuss/1329638/Python-Easy-DFS-MEMOIZATION-and-BFS by aatmsaat


'''

class Solution(object):
    def nearestExit(self, maze, entrance):
        """
        :type maze: List[List[str]]
        :type entrance: List[int]
        :rtype: int
        """
        
        m, n = len(maze), len(maze[0]) #row, col
        x, y = entrance
        
        #exit = border - 0*, *0, m*, *n
        exit = []
        
        for i in range(m):
            for j in range(n):
                if (i==0 or j==0 or i==m-1 or j==n-1) and maze[i][j] != '+' and (i!=x or j!=y): #if its the target and its not wall
                    #actually can not appending the list, but check everytime when it reach the location with th condition above.
                    exit.append([i, j]) 

        def dfs(i, j):
            #break and return 201 (max step) if one of these 3 condition = False #cannot find exit
            if not(0<=i<m and 0<=j<n and maze[i][j]=='.'): 
                return 201
            
            
            if [i,j] in exit:#can reach this exit, return 0 means end
                return 0
            
            maze[i][j] = '+' #visited then become wall, no need go back.
            
            ans = 1+min(dfs(i+1, j), dfs(i-1, j), dfs(i, j+1), dfs(i, j-1)) #4 directions
            
            maze[i][j] = '.' #convert back for future use
            
            return ans
        
        ans = dfs(x, y)
        
        if ans<201:
            return ans
        else:
            return -1

#BFS approach

'''
Reference: https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/discuss/1331038/Python-and-C%2B%2B-Solution-with-Explanation-BFS by vishnuSReddy

'''
class Solution(object):
    def nearestExit(self, maze, entrance):
        """
        :type maze: List[List[str]]
        :type entrance: List[int]
        :rtype: int
        """
        
        m, n = len(maze), len(maze[0]) #row, col
        x, y = entrance
        
        four_direction = [[0,1],[1,0],[-1,0],[0,-1]] #right, down, up, left
        
        #exit = border - 0*, *0, m*, *n
        exit = lambda i,j: (i==0 or j==0 or i==m-1 or j==n-1) and maze[i][j] != '+' and [i,j] != entrance
        
        #BFS approach
        
        #creating a queue
        maze[x][y] = '+' #mark the initial location as wall
        q = [entrance] #this will contain all possible steps in the future
        
        steps = 1
        while q:
            #visiting every q
            l = len(q)
            for k in range(l):
                i, j = q.pop(0)
                
                #four direction
                for row, col in four_direction:
                    new_i = i + row
                    new_j = j + col
                    
                    #skip if one of these 3 condition = False # out of border or met walls
                    #since this is checking first, so can mark visited at below
                    if not(0<=new_i<m and 0<=new_j<n and maze[new_i][new_j]=='.'): 
                        continue

                    if exit(new_i,new_j):#if reach exit
                        return steps
                    
                    maze[new_i][new_j] = '+' #visited then become wall, no need go back.

                    q.append([new_i, new_j])
                
            steps += 1 #after all q are pop, only increment by 1.

        return -1 #if the exit not found
