#Reference: https://leetcode.com/problems/minimum-operations-to-make-a-uni-value-grid/discuss/1513301/Java-or-Make-all-median

class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        
        array = [j for i in grid for j in i]
        array.sort()
        
        ans = 0
        med = array[len(array) // 2]
        
        for arr in array:
            temp = 0
            if arr != med:
                temp = abs(arr-med)
                if temp%x != 0:
                    return -1
                else:
                    temp = temp//x
                            
            ans += temp
        
        return ans