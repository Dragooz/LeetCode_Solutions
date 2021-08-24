#Reference: https://leetcode.com/problems/minimum-limit-of-balls-in-a-bag/discuss/1064548/JavaC%2B%2BPython-Binary-Search by lee215

class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        
        nums.sort()
        
        def check(val):
            max_ = maxOperations
            for num in nums[::-1]:
                if num<=val:
                    break
                    
                diff = (num-1)//val

                max_ -= diff
                if max_ < 0:
                    return False
                
            return True
        
        low = 1
        high = nums[-1]
        
        while low < high:
            mid = (high+low)//2
            
            if check(mid): #okay, then need lower val
                high = mid
            else:
                low = mid+1
                
        return low
      