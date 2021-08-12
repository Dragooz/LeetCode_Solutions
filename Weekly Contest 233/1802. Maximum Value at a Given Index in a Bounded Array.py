#Reference: https://leetcode.com/problems/maximum-value-at-a-given-index-in-a-bounded-array/discuss/1119801/JavaC%2B%2BPython-Binary-Search by lee215
class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        '''
        Binary Search: 
        while left < right:  
            mid = (left+right+1)//2
            
            if condition: #lesser, then increase
                left = mid
            else: #too much, reduce
                right = mid-1
        '''
        
        def test(a): #a = current guess peak
            b = max(a - index, 0) #the left most maximum val, from the peak index (the maximum is 0)
            res = (a + b) * (a - b + 1) / 2 #from {b, b+1... a}
            b = max(a - ((n - 1) - index), 0) #if est peak =4 at index 2, then index 3 will be only 3 and etc..
            res += (a + b) * (a - b + 1) / 2
            return res - a

        maxSum -= n #all integer suppose to be >=1, this makes all the integer >= 0, which makes calculation easier.
        
        #the answer lies between (0 and maxSum)+1
        left = 0
        right = maxSum
        
        while left < right: #use binary search to find
            mid = (left+right+1)//2
            
            if test(mid) <= maxSum: #if the case is valid, then increase the est peak
                left = mid
            else:
                right = mid-1 #else reduce
        
        return left+1