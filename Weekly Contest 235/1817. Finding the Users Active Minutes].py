import collections
class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        dict_ = collections.defaultdict(list)
        
        for id_, min_ in logs:
            dict_[id_].append(min_)
            
        uam = [len(set(val)) for key, val in dict_.items()]
            
        ans = [0] * k
        
        counter = collections.Counter(uam)
        
        for index, times in counter.most_common(): #loop through the counter
            ans[index-1] = times
            
        return ans