from collections import Counter
class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        
        count = Counter([(i[0]/i[1]) for i in rectangles])
        ans = 0
        for key in count.keys():
            ans += math.comb(count[key], 2)
            
        return ans