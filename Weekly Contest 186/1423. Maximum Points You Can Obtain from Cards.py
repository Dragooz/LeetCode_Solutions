#Reference: https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/discuss/597825/Simple-Clean-Intuitive-Explanation-with-Visualization

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        
        left_sum = [0] + list(accumulate(cardPoints))
        right_sum = [0] + list(accumulate(cardPoints[::-1]))
        
        ans = 0
        
        for i in range(k+1):
            
            left = left_sum[k-i]
            right = right_sum[i]
            
            ans = max(ans, left+right)
            
        return ans
        