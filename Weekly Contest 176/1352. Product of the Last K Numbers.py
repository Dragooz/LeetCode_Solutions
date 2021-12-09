class ProductOfNumbers:

    def __init__(self):
        self.numbers = [1]

    def add(self, num: int) -> None:
        if num!= 0:
            self.numbers.append(num * self.numbers[-1])
        else:
            self.numbers = [1] #reset here if 0

    def getProduct(self, k: int) -> int:
        if k >= len(self.numbers):
            return 0
        return self.numbers[-1] // self.numbers[-k-1]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)