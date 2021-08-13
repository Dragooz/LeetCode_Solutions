#Reference: https://leetcode.com/problems/maximum-average-pass-ratio/discuss/1108263/PythonJava-Max-Heap-Clean-and-Concise by hiepit

import heapq
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        
        def get_profit(a,b):
            return (a+1)/(b+1) - a/b
        
        profit = [[-get_profit(a,b), a, b] for a, b in classes]
        
        heapq.heapify(profit)
        
        for _ in range(extraStudents):
            _, a, b = heapq.heappop(profit)
            heapq.heappush(profit, [-get_profit(a+1,b+1), a+1 , b+1])
        
        return sum([a/b for _, a ,b in profit]) / (len(profit))
        
        