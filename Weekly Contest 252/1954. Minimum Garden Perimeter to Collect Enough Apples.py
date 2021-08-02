class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        #Apples = number of rows of apple * ([1+2+3..+max coor, which is peri/2] = max coor/2 * 1+max coor) *2
        
        peri = 2
        apples = (peri+1) * (peri/2) * (1+peri/2) *2
        
        while neededApples > apples:
            peri += 2
            apples = (peri+1) * (peri/2) * (1+peri/2) *2
            
        return peri*4