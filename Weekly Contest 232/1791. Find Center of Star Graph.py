from collections import Counter
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        counter = Counter()
        for l in edges:
            for num in l:
                counter[num] +=1
        
        return counter.most_common(1)[0][0]