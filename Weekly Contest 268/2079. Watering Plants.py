class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        
        temp = capacity
        steps = 0
        
        for i in range(len(plants)):
            
            if temp < plants[i]:
                steps += (i+1)*2 -2
                temp = capacity
            
            if temp >= plants[i]:
                steps += 1
                temp -= plants[i]
                
        return steps