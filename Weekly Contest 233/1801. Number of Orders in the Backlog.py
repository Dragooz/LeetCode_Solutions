#Reference: https://leetcode.com/problems/number-of-orders-in-the-backlog/discuss/1119992/JavaC%2B%2BPython-Priority-Queue by lee215

import heapq
class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        
        sell = []
        buy = []
        
        for order in orders:
            price, amount, type_ = order
            
            if type_ ==1: #sell
                heappush(sell, [price, amount]) #b
            else:
                heappush(buy, [-price, amount])
                
            while sell and buy and sell[0][0] <= -buy[0][0]:

                min_ = min(sell[0][1], buy[0][1])

                sell[0][1] -= min_
                buy[0][1] -= min_

                if sell[0][1] == 0:
                    heappop(sell)
                if buy[0][1] == 0:
                    heappop(buy)
                
        return sum(a for _, a in sell+buy) % (10**9 +7)
        
        
                
        