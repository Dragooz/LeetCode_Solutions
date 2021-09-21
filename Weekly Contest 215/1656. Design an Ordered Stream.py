import heapq

class OrderedStream:

    def __init__(self, n: int):
        self.chunk = n
        self.list_ = []
        self.cur = 1

    def insert(self, idKey: int, value: str) -> List[str]:
        ans = []
        heapq.heappush(self.list_, [idKey, value])
        # print(self.list_)
        if self.list_[0][0] == self.cur:
            while self.list_:
                id_, val = heapq.heappop(self.list_)
                # print('popped:', id_, val)
                self.cur = id_ + 1
                ans.append(val)
                
                if self.list_:
                    if self.cur != self.list_[0][0]:
                        break
                else:
                    break
                
        return ans


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)