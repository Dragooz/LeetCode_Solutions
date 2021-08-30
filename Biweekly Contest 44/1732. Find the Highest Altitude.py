class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans = 0
        temp= 0
        for g in gain:
            temp += g 
            ans = max(ans, temp)
            
        return ans