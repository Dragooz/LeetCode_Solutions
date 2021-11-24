class Solution:
    def countLargestGroup(self, n: int) -> int:
        d = defaultdict(int)
        
        for i in range(1,n+1):
            d[sum([int(j) for j in str(i)])] +=1
        
        d = sorted(d.items(), key=lambda kv: kv[1], reverse=True)
        
        max_val = d[0][1]
        ans = 0
        
        for key, val in d:
            if val == max_val:
                ans+=1
            else:
                break
                
        return ans