class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = deque()
        self.max_size = maxSize

    def push(self, x: int) -> None:
        if self.max_size > len(self.stack):
            self.stack.append(x)
        else:
            pass

    def pop(self) -> int:
        if self.stack:
            return self.stack.pop()
        else:
            return -1

    def increment(self, k: int, val: int) -> None:
        
        min_ = min(k, len(self.stack))
        
        for i in range(min_):
            self.stack[i] += val
            

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)