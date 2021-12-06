#Reference: https://leetcode.com/problems/finding-3-digit-even-numbers/discuss/1611987/Python3-brute-force

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        
        digits.sort()
        ans = set()
        for x,y,z in permutations(digits, 3):
            if x!=0 and z%2 == 0:
                ans.add(x*100 + y*10 + z)
     
        return sorted(ans)