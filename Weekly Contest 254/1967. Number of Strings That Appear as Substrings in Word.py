import collections

class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        ans = 0
        memo = collections.defaultdict(list)
        for p in patterns:
            n = len(p)
            
            if memo[p] == 1:
                ans+=1
            elif memo[p] ==0:
                continue
            else:
                for i in range(0, len(word)-n+1):
                    if p == word[i:i+n]:
                        memo[p] = 1
                        ans +=1
                        break
                if memo[p] == []:
                    memo[p] = 0
        return ans