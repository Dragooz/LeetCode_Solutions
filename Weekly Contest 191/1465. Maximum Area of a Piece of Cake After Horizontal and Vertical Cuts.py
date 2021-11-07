class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        
        mod = 10**9 + 7
        
        horizontalCuts.sort()
        verticalCuts.sort()
        
        horizontalCuts = [0] + horizontalCuts + [h]
        verticalCuts = [0] + verticalCuts + [w]
        max_height = max([j - i for i ,j in zip(horizontalCuts[0:-1], horizontalCuts[1:])])
        max_width = max([j - i for i, j in zip(verticalCuts[0:-1], verticalCuts[1:])])
        
        return (max_height * max_width) % mod