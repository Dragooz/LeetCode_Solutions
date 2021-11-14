class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        
        ans = tickets[k]
        
        for left in tickets[:k]:
            ans += min(tickets[k], left)
            
        for right in tickets[k+1:]:
            val = min(tickets[k], right)
            if val == tickets[k]:
                ans+= val-1
            else:
                ans+=val
                
        return ans