#https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/discuss/686316/JavaC%2B%2BPython-Binary-Search

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        
        total_flower = m*k
        if total_flower > len(bloomDay):
            return -1
        
        left, right = 1, max(bloomDay)
        
        while left < right:
            
            mid = (left + right) // 2
            
            bouque = 0
            flower = 0
            for bd in bloomDay:
                if bd > mid:
                    flower = 0
                else:
                    flower += 1
                
                if flower >= k:
                    bouque +=1 
                    flower = 0
                    if bouque == m:
                        break
                        
            if bouque == m:
                right = mid
            else:
                left = mid+1
                    
        return left
            
            