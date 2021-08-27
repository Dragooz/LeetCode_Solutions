from collections import Counter

class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        
        count = Counter()
        
        for i in range(lowLimit, highLimit+1):
            count[sum(int(j) for j in str(i))] +=1
            
        return count.most_common(1)[0][1]