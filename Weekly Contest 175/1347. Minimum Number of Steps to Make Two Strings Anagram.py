class Solution:
    def minSteps(self, s: str, t: str) -> int:
        
        count_s = Counter(s)
        count_t = Counter(t)
        
        for key, val in count_t.most_common():
            count_s[key] -= count_t[key]
            count_s[key] = max(0, count_s[key])
            
        ans = 0
        for _, val in count_s.most_common():
            ans += val
            
        return ans