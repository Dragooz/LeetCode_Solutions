from collections import Counter
class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        #main idea: count every possible year
        logs = sorted(logs)
        
        count = Counter()
        for start, end in logs:
            count.update([i for i in range(start,end)])
        
        return count.most_common()[0][0]