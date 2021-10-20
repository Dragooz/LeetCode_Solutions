#Reference: https://leetcode.com/problems/find-the-winner-of-an-array-game/discuss/768007/JavaC%2B%2BPython-One-Pass-O(1)-Space

class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        
        cur = arr[0]
        win = 0
        for i in range(1, len(arr)):
            if arr[i]> cur:
                cur = arr[i]
                win = 0
            win+=1 #tracking win of cur
            if win == k:
                break
                
        return cur
        
        