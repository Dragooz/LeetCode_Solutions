class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        
        dest = [i[1] for i in paths]
        
        c = Counter([j for i in paths for j in i])
        
        for key, val in c.most_common()[::-1]:
            if val == 1 and key in dest:
                return key
            