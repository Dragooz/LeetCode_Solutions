class Solution:
    def checkOverlap(self, radius: int, x_center: int, y_center: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        
        #move circle to center (0,0)
        x1 -= x_center
        x2 -= x_center
        y1 -= y_center
        y2 -= y_center
        
        if x1*x2 > 0:  #both neg or both pos
            min_x = min(x1**2, x2**2)
        else:
            min_x = 0
            
        if y1*y2 > 0:
            min_y = min(y1**2, y2**2)
        else:
            min_y = 0
            
        return min_y + min_x <= radius**2 #whether the circle reach the nearest edge of the square