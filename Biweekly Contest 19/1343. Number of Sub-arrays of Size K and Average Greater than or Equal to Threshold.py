class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        n = len(arr)
        prefix_sum = [0] + list(accumulate(arr))
        
        ans = 0
        for i in range(n-k+1):
            
            if (prefix_sum[i+k]-prefix_sum[i]) / k >= threshold:
                ans+=1
                
        return ans