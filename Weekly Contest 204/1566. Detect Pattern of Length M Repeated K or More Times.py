class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        
        for i in range(len(arr)-m):
            word = arr[i:i+m]*k
            for j in range(i, len(arr)-m):
                if arr[j: j+len(word)] == word:
                    return True
            
        return False