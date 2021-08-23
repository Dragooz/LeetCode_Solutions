class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        
        ans = []
        
        for index1, _ in enumerate(boxes):
            temp_ans = 0
            for index2, val2 in enumerate(boxes):
                if val2 == '1':
                    temp_ans += abs(index2 - index1)
            
            ans.append(temp_ans)
            
        return ans