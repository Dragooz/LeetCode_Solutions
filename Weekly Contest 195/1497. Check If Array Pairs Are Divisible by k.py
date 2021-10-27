#Reference: https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/discuss/709691/Java-7ms-Simple-Solution

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        
        arr = [i%k for i in arr]
        count = Counter(arr)
        
        for key, val in count.most_common():
            if key == 0:
                if count[0]%2 != 0:
                    return False 
            else:
                if count[key] != count[k-key]:
                    return False
                
        return True