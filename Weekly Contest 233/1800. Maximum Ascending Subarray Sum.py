class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        ans = []
    
        n = len(nums)
        prev= nums[0]
        temp_ans = prev
        
        for i in range(1, n):
            if nums[i] > prev:
                temp_ans += nums[i]
            else:
                ans.append(temp_ans)
                temp_ans = nums[i]
                
            prev = nums[i]
            
        ans.append(temp_ans)
            
        return max(ans)