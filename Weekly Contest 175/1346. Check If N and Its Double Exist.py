class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        
        for index, i in enumerate(arr):
            if i*2 in arr[:index] + arr[index+1:]:
                return True
            
        return False