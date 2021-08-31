class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        
        squares = [min(i[0], i[1]) for i in rectangles]
        
        max_ = max(squares)
        
        ans = 0 
        
        for j in squares:
            if j == max_:
                ans+=1
                
        return ans