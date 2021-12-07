class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        
        middle = math.ceil(sqrt(num+2))
        
        for i in range(middle, 1, -1):
            if (num+1)%i == 0:
                return [(num+1)//i, i]
            
            if (num+2)%i == 0:
                return [(num+2)//i, i]