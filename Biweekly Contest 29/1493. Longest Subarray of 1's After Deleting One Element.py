class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        if 0 not in nums:
            return len(nums)-1
        
        ans = 0
        temp = 0
        tempp = 0
        quota=True
        
        for num in nums:
            
            if num==1:
                if not quota:
                    tempp+=1
                temp+=1
                
            else:
                if quota:
                    quota=False
                else:
                    ans = max(ans, temp)
                    temp = tempp
                    tempp = 0
        
        ans = max(ans, temp)
                    
        return ans
                