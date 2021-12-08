class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n = n
        self.counter = 0
        self.pp = {i:j for i, j in zip(products, prices)}
        self.discount = discount

    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.counter += 1
        
        bills = 0
        for p, a in zip(product, amount):
            bills += self.pp[p] * a
            
        if self.counter == self.n:
            self.counter = 0
            bills = bills * ((100-self.discount) / 100)
        
        return bills


# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)