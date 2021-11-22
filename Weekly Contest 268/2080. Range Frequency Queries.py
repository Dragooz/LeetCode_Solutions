#Reference: https://leetcode.com/problems/range-frequency-queries/discuss/1589201/Python-Binary-Search

class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.arr = defaultdict(list)
        for index, a in enumerate(arr):
            self.arr[a].append(index)

    def query(self, left: int, right: int, value: int) -> int:
        i = bisect.bisect(self.arr[value], left-1)
        j = bisect.bisect(self.arr[value], right)
        return j-i
        

# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)