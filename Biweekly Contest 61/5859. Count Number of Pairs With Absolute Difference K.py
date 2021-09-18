class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        
        ans=0
        for i in range(n):
            for j in range(i+1, n):
                if abs(nums[j]-nums[i]) == k:
                    ans+=1
                    
        return ans