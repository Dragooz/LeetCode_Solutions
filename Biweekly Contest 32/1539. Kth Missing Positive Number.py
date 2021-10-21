class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        
        nums = [i for i in range(1, 2001)]
        
        ans = 0
        for num in nums:
            if num not  in arr:
                ans+=1
            
            if ans == k:
                return num
        
        