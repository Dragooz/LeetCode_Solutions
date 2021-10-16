class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        
        for i in range(len(arr)-2):
            # print(arr[i:i+3])
            if all(j%2==1 for j in arr[i:i+3]):
                return True
            
        return False
            