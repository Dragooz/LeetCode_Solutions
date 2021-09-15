#Reference: https://leetcode.com/problems/find-the-most-competitive-subsequence/discuss/952786/JavaC%2B%2BPython-One-Pass-Stack-Solution by lee215

class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        
        stack = []
        
        for index, num in enumerate(nums):
            #while stack, and the last element in stack is bigger than the num
            #and after popping from the stack, the total remaining elements still >= k
            while stack and stack[-1] > num and len(stack) -1 + len(nums)-index >= k:
                stack.pop()
            
            if len(stack) < k:
                stack.append(num)
                
        return stack