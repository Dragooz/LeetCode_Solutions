class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        
        ans = 0
        for index, color in enumerate(colors):
            for index2 in range(index, len(colors)):
                if colors[index] != colors[index2]:
                    ans = max(ans, index2-index)
                    
        return ans