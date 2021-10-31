#Reference: https://leetcode.com/problems/minimum-operations-to-convert-number/discuss/1550007/Python3-bfs

class Solution:
    def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:
        
        seen = set()
        operations = [add, sub, xor]
        queue = [start]
        ans = 0
        
        while queue:
            
            for _ in range(len(queue)):
                val = queue.pop(0)
                
                if val == goal:
                    return ans

                if 0 <= val <= 1000:
                    for num in nums:
                        for op in operations:
                            res = op(val, num)

                            if res not in seen:
                                seen.add(res)
                                queue.append(res)

            ans+=1
            
        return -1
                        
        
        
        