#Reference: https://leetcode.com/problems/detect-squares/discuss/1471908/O(n)-Solution-Explained

from collections import defaultdict
class DetectSquares:

    def __init__(self):
        self.coor = defaultdict(int)
        self.points = []

    def add(self, point: List[int]) -> None:
        self.coor[tuple(point)] +=1
        self.points.append(point)

    def count(self, point: List[int]) -> int:
        
        ans=0
        px, py = point
        for x, y in self.points:
            if (abs(py-y) != abs(px-x)) or px==x or py==y: #checking diagonal
                continue
            ans += self.coor[(x, py)] * self.coor[(px, y)]
            
        return ans


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)