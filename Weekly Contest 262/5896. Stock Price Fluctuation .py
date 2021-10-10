#Reference: https://leetcode.com/problems/stock-price-fluctuation/discuss/1513293/Python-Clean-2-Heaps-Commented-Code

class StockPrice:

    def __init__(self):
        self.stock = {}
        self.latest = 0
        
        self.max_stock = []
        self.min_stock = []

    def update(self, timestamp: int, price: int) -> None:
        
        self.latest = max(self.latest, timestamp)
        
        self.stock[timestamp] = price
         
        heappush(self.max_stock, (-price, timestamp))
        heappush(self.min_stock, (price, timestamp))
        
    def current(self) -> int:
        return self.stock[self.latest]

    def maximum(self) -> int:
        cur_price, time = heappop(self.max_stock)
        
        while -cur_price != self.stock[time]:
            cur_price, time = heappop(self.max_stock)
            
        heappush(self.max_stock, (cur_price, time))
        return -cur_price
        
    def minimum(self) -> int:
        cur_price, time = heappop(self.min_stock)
        
        while cur_price != self.stock[time]:
            cur_price, time = heappop(self.min_stock)
            
        heappush(self.min_stock, (cur_price, time))
        return cur_price
    

# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()