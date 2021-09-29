#Reference: https://leetcode.com/problems/coordinate-with-maximum-network-quality/discuss/898698/Clean-Python-3-straightforward

class Solution:
    def bestCoordinate(self, towers: List[List[int]], radius: int) -> List[int]:
        
        n = len(towers)
        ans = [0, 0, 0] #quality, x, y
        
        for c in range(51):
            for r in range(51):
                quality = 0
                for x, y, q in towers:
                    d = sqrt( (y-r)**2 + (x-c)**2 )

                    if d <= radius:
                        quality += math.floor((q / (1 + d)))

                if ans[0] < quality:
                    ans = [quality, c, r]
                elif ans[0] == quality:
                    if ans[1] > c:
                        ans = [quality, c, r]
                    elif ans[1] == c:
                        if ans[2] > r:
                            ans = [quality, c, r]
                            
        return [ans[1], ans[2]]
            
        