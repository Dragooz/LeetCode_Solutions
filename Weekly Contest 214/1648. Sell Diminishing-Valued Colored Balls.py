#Reference: https://leetcode.com/problems/sell-diminishing-valued-colored-balls/discuss/927560/C%2B%2B-Binary-Answer-or-Sort%2BGreedy

class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        
        valid = lambda x: sum([max(0, xx-x) for xx in inventory])
        
        low, high = 0, 10**9
        
        while low < high:
            mid = (low + high + 1) // 2
            
            if valid(mid) >= orders:
                low = mid
            else:
                high = mid - 1
        
        # n/2 * (a + l) 
        
        ans = 0
        
        for x in inventory:
            if x > low:
                ans += ((low+x +1) * (x-low))//2 
    
        ans = ans- ((valid(low) - orders)*(low+1))
        
        return ans % (10**9 +7)
            