import collections
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        counter = collections.Counter(s)
        
        list_ = [k for _, k in counter.most_common()]
        return list_[0] == sum(list_)/len(list_)