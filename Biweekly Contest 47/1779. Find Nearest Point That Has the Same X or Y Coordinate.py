class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        
        points = [[a, b, index] for index, (a,b) in enumerate(points) if a==x or b==y]
        
        if len(points) == 1:
            return points[0][2]
        elif len(points) == 0:
            return -1
        
        print(points)
        
        min_ = sys.maxsize
        index = 0
        
        for i in range(len(points)):
            
            diff = abs(points[i][0] -x) + abs(points[i][1] -y)
            if diff < min_:
                index = points[i][2]
                min_ = diff

        return index