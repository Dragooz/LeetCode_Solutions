class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        
        ans = []
        arr.sort()
        d = defaultdict(list)
        
        for a in arr:
            string = str(bin(a))[2:]

            ones = sum([int(i) for i in string])
            
            d[ones].append(a)
        
        s = sorted(d.items(), key=lambda x:(x[0], x[1]))
        
        print(s)
        
        for k, v in s:
            ans += v
            
        return ans
            
            
                