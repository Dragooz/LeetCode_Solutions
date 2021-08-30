#Reference from: https://leetcode.com/problems/minimum-number-of-people-to-teach/discuss/1031079/Python-3-steps

from collections import Counter

class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        languages = [set(l) for l in languages]
        
        users = set()
        for u, v in friendships:
            u = u-1
            v = v-1
            
            if languages[u] & languages[v]: continue
            users.add(u)
            users.add(v)
            
        langCount = Counter()
        
        for user in users:
            for lang in languages[user]:
                langCount[lang] += 1
                
        return len(users) - max(langCount.values(), default=0) #number of users - majority of users that know the most popular lang