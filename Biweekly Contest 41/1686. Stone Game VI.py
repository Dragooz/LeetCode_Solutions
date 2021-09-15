class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        
        sum_ = [a+b for a, b in zip(aliceValues, bobValues)]
        
        index_list = [i[0] for i in sorted(enumerate(sum_), key=lambda x: x[1], reverse=True)]

        a = 0
        b = 0
        
        for i, index in enumerate(index_list):
            if i % 2 == 0:
                a += aliceValues[index]
                
            else:
                b += bobValues[index]
                
        if a==b:
            return 0
        elif a>b:
            return 1
        else:
            return -1
            