#Reference: https://leetcode.com/problems/minimum-adjacent-swaps-to-reach-the-kth-smallest-number/discuss/1186823/Python-3-brute-force
#by lenchen1112

class Solution:
    def getMinSwaps(self, num: str, k: int) -> int:
        #main idea: 
        #get the next permu
        #return the number of adj swaps
        
        n = len(num)
        num = list(num)
        
        def nxt_perm(num: list) -> list:
            i = n - 1
            while i > 0 and num[i-1] >= num[i]:
                i -= 1
            j = i
            while j < n and num[i-1] < num[j]:
                j += 1
            num[i-1], num[j-1] = num[j-1], num[i-1]
            num[i:] = num[i:][::-1] # credit to @ye15, reduce time from nlogn to n
            return num
        
        nxt_k_num = list(num)
        
        for _ in range(k):
            nxt_k_num = nxt_perm(nxt_k_num)
            
        ans = 0
        for i in range(n):
            j = i
            while j<n and nxt_k_num[i] != num[j]: #nums need to become k_nums, so the moving j should be refer to num
                j +=1
            
            ans += j-i #adjacent digit swaps, so j-i
            num[i:j+1] = [num[j]] + num[i:j]
            
        return ans
            
            
            
            
            
            
            
            
            
            
            
        