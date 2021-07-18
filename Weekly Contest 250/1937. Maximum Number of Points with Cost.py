#Reference:
#https://leetcode.com/problems/maximum-number-of-points-with-cost/discuss/1344908/Python-3-DP-Explanation-with-pictures. by Bakerston

#too slow: O(N^2 * m-1)
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        
        m = len(points) #cols
        n = len(points[0]) #rows
        #main idea:
        #create an curr list, that track the cumulative score
        #loop through the rows, get the curr list update.
        curr = [0]*n
        prev = points[0]
        
        if m==1: return max(points[0]) #1 col
        if n==1: return sum([point[0] for point in points]) #only 1 row
        
        for a in range(m-1): #first row didn't count
            for b in range(n):
                curr[b] = max( [prev[b_sec] - abs(b_sec-b) for b_sec in range(n)])  + points[a+1][b]
            prev = curr[:]
        
        print(curr)
        return max(curr)

#modified:
#to understand deeper, please visit the reference.
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        
        m = len(points) #cols
        n = len(points[0]) #rows
        
        #main idea:
        #create an curr list, that track the cumulative score
        #for each rows, create a max val list from left and right
        #to update curr[i], get the max val from both left[i] and right[i] , plus the current row[i]
        
        if m==1: return max(points[0]) #1 col
        if n==1: return sum([point[0] for point in points]) #only 1 row
        
        def create_lft_max(arr):
            lft = [arr[0]] + (len(arr)-1) * [0] #remain index 0, since the first always the max
            
            for i in range(1, len(arr)):
                lft[i] = max(arr[i], lft[i-1] -1)
                
            return lft
            
        def create_rgt_max(arr):
            rgt = (len(arr)-1) * [0] + [arr[-1]] #remain the last index, since the last always the max
            
            for i in range(len(arr)-2, -1, -1): #start from rightmost second element, till -1, stepsize = -1
                rgt[i] = max(arr[i], rgt[i+1] -1 )
                
            return rgt
        
        curr = [0]*n #final cumulative scoring list
        prev = points[0] #prev row
        
        for i in range(m-1): #first row doesn't count:
            lft, rgt = create_lft_max(prev), create_rgt_max(prev)
            for j in range (n): #each row's element
                curr[j] = points[i+1][j] + max(lft[j], rgt[j])
            prev = curr[:] #update prev
            
        return max(curr)
    

    