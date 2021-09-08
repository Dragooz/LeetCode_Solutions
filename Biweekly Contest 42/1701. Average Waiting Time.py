class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        
        time = 0
        
        ans = 0
        
        for c in customers:
            time = max(time, c[0])
            time += c[1]

            ans += time - c[0]
            
        return ans/len(customers)