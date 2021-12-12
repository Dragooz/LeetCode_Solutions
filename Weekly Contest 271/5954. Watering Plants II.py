class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        
        n = len(plants)
        mid = 0
        
        ans= 0
        ac = capacityA
        bc = capacityB
        
        while len(plants) >=2:
            
            left = plants.pop(0)
            right = plants.pop(-1)
            
            if left > ac:
                ac = capacityA - left
                ans+=1
            else:
                ac -= left

            if right > bc:
                bc = capacityB - right
                ans+=1
            else:
                bc -= right
                
        if plants:
            if ac >= plants[0] or bc >= plants[0]:
                return ans
            else:
                return ans+1
        else:
            return ans
            