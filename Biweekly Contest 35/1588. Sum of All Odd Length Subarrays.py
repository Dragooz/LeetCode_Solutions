class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        
        gap = 1
        ans = 0
        while gap <= len(arr):
            i = 0
            while i+gap <= len(arr):
                ans += sum(arr[i:i+gap])
                # print(ans)
                i+=1
            gap+=2
        
        return ans