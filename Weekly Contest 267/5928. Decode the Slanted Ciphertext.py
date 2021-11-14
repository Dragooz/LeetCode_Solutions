class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        
        n = len(encodedText)
        cols = n//rows
        graph = [[0] * cols for i in range(rows)]
        
        for i in range(rows):
            for j in range(cols):
                graph[i][j] = encodedText[(i*cols)+j]
                
                
        ans = ''
        for i in range(cols):
            ii = i
            for j in range(rows):

                if len(graph) > j and len(graph[0]) >ii:
                    ans += graph[j][ii]
                    ii+=1
                    
        return ans.rstrip()