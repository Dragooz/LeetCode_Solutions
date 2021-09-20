  
class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        
        n = len(nums)
        ans = 0
        
        ans_bool = []
        ans_bool.append(False)
        
        max_ = 0
        for i in range(1, n-1):
            max_ = max(max_, nums[i-1]) 
            if max_ >= nums[i]: #invalid
                ans_bool.append(False)
            else:
                ans_bool.append(True)
                
        ans_bool.append(False)
        
        min_ = math.inf
        for i in range(n-2, 0, -1):
            min_ = min(min_, nums[i+1]) 
            if min_ <= nums[i]: #invalid
                ans_bool[i] = False

        for i in range(1, n-1):
            if ans_bool[i] ==True:
                ans+=2
            else:
                if nums[i-1] < nums[i] < nums[i+1]:
                    ans+=1
                
        return ans