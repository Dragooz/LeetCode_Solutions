#Reference: https://leetcode.com/problems/check-if-move-is-legal/discuss/1389343/Clean-Code-Explanation by anaccountforlc2

class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:

        n, m = len(board), len(board[0])
        
        direction = [[0,1], [1,0], [0, -1], [-1, 0], 
                     [1, 1], [1, -1], [-1, 1], [-1,-1]]
        
        board[rMove][cMove] = color
        
        def legal(row, col, dr, color):
            r, c = dr
            row += r
            col += c
            length = 1
            
            while 0<=row< n and 0<=col < m:
                length+=1
                if board[row][col] == color:
                    return length >=3
                elif board[row][col] == '.':
                    return False
                else: #continue
                    row+= r
                    col+= c
                    
                
            
            return False
        
        for d in direction:
            if legal(rMove, cMove, d, color):
                return True
        
        return False
            
            