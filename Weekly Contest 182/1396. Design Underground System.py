#Reference: https://leetcode.com/contest/weekly-contest-182/problems/design-underground-system/

class UndergroundSystem:

    def __init__(self):
        self.place = defaultdict(list)
        self.check = defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check[id] = [t, stationName]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        
        time_taken = t- self.check[id][0]
        self.place[(self.check[id][1], stationName)].append(time_taken)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return sum(self.place[(startStation, endStation)]) / len(self.place[(startStation, endStation)])


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)