#first attempt: time limit exceed.
class SeatManager:
    def __init__(self, n: int):
        self.mask = [0] * len([i for i in range(n)])

    def reserve(self) -> int:
        for index, m in enumerate(self.mask):
            if m == 0:
                self.mask[index] = 1
                break
                
        return index+1

    def unreserve(self, seatNumber: int) -> None:
        self.mask[seatNumber-1] = 0
        


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)

#second attempt: using heap
#reference: https://leetcode.com/problems/seat-reservation-manager/discuss/1185886/C%2B%2B-Set-vs.-Max-Reserved-Seat by votrubac
import heapq
class SeatManager:
    #use min heap
    def __init__(self, n: int):
        self.heap = [i for i in range(1, n+1)] #already sorted, not need heapify.

    def reserve(self) -> int:
        return heapq.heappop(self.heap)

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.heap, seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)