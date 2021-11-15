#Reference: https://leetcode.com/problems/most-beautiful-item-for-each-query/discuss/1576050/Python-4-lines-Solution

class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        
        items = sorted(items + [[0,0]])
        
        for i in range(len(items) -1):
            items[i+1][1] = max(items[i][1], items[i+1][1])
        
        ans = []
        for q in queries:
            index = bisect.bisect(items, [q+1]) - 1
            b = items[index][1]
            ans.append(b)
            
        return ans
            
            
            
            
            
        