#Reference: https://leetcode.com/problems/check-array-formation-through-concatenation/discuss/918408/Python-5-lines-hashmap

class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        
        mp = {x[0]: x for x in pieces}
        
        ans = []
        for num in arr:
            ans += mp.get(num, [])
    
        return ans == arr