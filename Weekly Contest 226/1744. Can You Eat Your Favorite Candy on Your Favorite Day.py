#Reference from: https://leetcode.com/problems/can-you-eat-your-favorite-candy-on-your-favorite-day/discuss/1042904/C%2B%2B-Java-Python-Simple-Explanation-O(N) by sachuverma

class Solution:
    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        
        ans = []
        
        prefix_sum = [0] * (len(candiesCount)+1)
        
        for i in range(len(candiesCount)):
            prefix_sum[i+1] = prefix_sum[i] + candiesCount[i]
        
        for q in queries:
            type_, day, cap = q
            
            candies_need_to_eat = prefix_sum[type_]
            if cap*(day+1) > candies_need_to_eat and day < prefix_sum[type_+1]: #max and min
                ans.append(True)
            else:
                ans.append(False)
                
        return ans