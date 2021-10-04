class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        
        def to_minute(kt):
            return (int(kt[0:2]) * 60) + int(kt[3:])
        
        names = defaultdict(list)
        
        ans = set()
        
        for kn, kt in zip(keyName, keyTime):
            names[kn].append(to_minute(kt))
            
        for key, val in names.items():
            val = sorted(val)
            i = 2
            while i< len(val):

                if val[i-2] <= val[i] and val[i] - val[i-2] <= 60:
                    ans.add(key)
                    break
                i+=1
                
        return sorted(ans)
                
            
            
        