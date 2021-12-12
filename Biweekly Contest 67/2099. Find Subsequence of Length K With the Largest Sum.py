class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        
        sorted_ = sorted(nums, reverse=True)[:k]
        
        ans =[]
        for num in nums:
            if num in sorted_:
                ans.append(num)
                sorted_.remove(num)
                
        return ans