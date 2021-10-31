#Reference: https://leetcode.com/problems/plates-between-candles/discuss/1549018/JavaC%2B%2BPython-Binary-Search-and-O(Q-%2B-N)-Solution

class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        
        ans = []
        
        candles = [index for index, c in enumerate(s) if c=='|']
        print(candles)
        for q in queries:
            start, end = q
            
            i = bisect.bisect_left(candles, start)
            j = bisect.bisect(candles, end) - 1
            
            ans.append(candles[j] - candles[i] - (j-i) if i<j else 0)
            
        return ans