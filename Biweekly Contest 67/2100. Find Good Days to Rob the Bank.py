#Reference: https://leetcode.com/problems/find-good-days-to-rob-the-bank/discuss/1623415/Python-Explanation-with-pictures-DP

class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        
        if time == 0:
            return list(range(len(security)))
        
        left, right , n = [1], [1], len(security)
        
        #build non-increasing
        curr = 1
        for i in range(1, n):
            if security[i-1] >= security[i]: #ok
                curr+=1
            else:
                curr=1
            left.append(curr)
            
        #build non-decreasing
        curr = 1
        for i in range(n-2, -1, -1):
            if security[i] <= security[i+1]:
                curr+=1
            else:
                curr=1
            right.append(curr)
            
        right.reverse()
        
        return [i for i in range(n) if left[i] >= time+1 and right[i] >= time+1]