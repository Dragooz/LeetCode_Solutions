class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        
        list_ = []
        ans = 0
        seen = set()
        
        for num in nums:
            if num in seen:
                ans = max(ans, sum(list_))
                while num in seen:
                    seen.remove(list_.pop(0))
                
            list_.append(num)
            seen.add(num)
        
        ans = max(ans, sum(list_))
            
            
        return ans