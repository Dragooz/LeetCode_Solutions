class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        
        prefix_sum = [0] + list(accumulate(nums))
        ans = []
        for i in range(len(nums)):
            
            if i-k >= 0 and k+i < len(nums): #valid
                result = (prefix_sum[(i+k+1)] - prefix_sum[i-k]) // ((k*2)+1)
                ans.append(result)
            else:
                ans.append(-1)
        
        return ans