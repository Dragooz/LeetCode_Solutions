class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        
        boxTypes.sort(key=lambda x: (-x[1], -x[0]))
        
        print(boxTypes)
        
        ans = 0
        
        for box, unit in boxTypes:
            
            for _ in range(box):
                ans += unit
                truckSize -= 1
                
                if truckSize == 0:
                    return ans
                
        return ans