class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        
        def shop_needed(num):
            return sum(math.ceil(i/num) for i in quantities)
        
        low = math.ceil(sum(quantities) / n)
        high = max(quantities)
        
        while low <= high:
            mid = (low + high) // 2
            
            if shop_needed(mid) > n: 
                low = mid + 1
            else:
                high = mid - 1
            
        return low