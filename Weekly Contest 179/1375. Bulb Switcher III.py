#Reference: https://leetcode.com/problems/bulb-switcher-iii/discuss/532538/JavaC%2B%2BPython-Straight-Forward-O(1)-Space

class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        
        ans = 0
        right_most_lighten = 0
        
        for count, num in enumerate(light, 1):
            
            right_most_lighten = max(right_most_lighten, num)
            
            if right_most_lighten == count: #all lighten on the left side
                ans+=1
            
        return ans
            