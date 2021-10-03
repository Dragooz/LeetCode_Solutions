#Reference: https://leetcode.com/problems/stone-game-ix/discuss/1500245/JavaC%2B%2BPython-Easy-and-Concise-6-lines-O(n)

class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        
        n = len(stones)
        total = 0
        cnt = Counter([i%3 for i in stones])

        if min(cnt[1], cnt[2]) == 0: # either one is 0
            return max(cnt[1], cnt[2]) > 2 and cnt[0] % 2 == 1 # either is 1+1+1 or 2+2+2 that will allow alice to win, given that the 0 is odd. Because Alice > Bob > Alice > Bob 
        return abs(cnt[1] - cnt[2]) > 2 or cnt[0] % 2 == 0 # 
    
#         if sum(count) % 2 == 0:
#             return True
#         else:
#             return False
            
                
            
        