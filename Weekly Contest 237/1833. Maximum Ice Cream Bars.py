class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        i = 0
        while coins >= 0 and i < len(costs):
            coins -= costs[i]
            if coins >= 0:
                i +=1
            else:
                return i
            
        return i
            
            