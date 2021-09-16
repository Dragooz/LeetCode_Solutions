from collections import deque
class FrontMiddleBackQueue:

    def __init__(self):
        self.queue = deque([])

    def pushFront(self, val: int) -> None:
        self.queue.appendleft(val)
        # print(self.queue)
        
    def pushMiddle(self, val: int) -> None:
        index = (len(self.queue)//2)
        self.queue.insert(index, val)
        # print(self.queue)

    def pushBack(self, val: int) -> None:
        self.queue.append(val)
        # print(self.queue)

    def popFront(self) -> int:
        if self.queue:
            return self.queue.popleft()
        return -1

    def popMiddle(self) -> int:
        if len(self.queue) % 2 == 0:
            index = (len(self.queue)//2) -1
        else:
            index = (len(self.queue)//2)
        if self.queue:
            temp = self.queue[index]
            del self.queue[index]
            return temp
        else:
            return -1

    def popBack(self) -> int:
        if self.queue:
            return self.queue.pop()
        return -1

# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()