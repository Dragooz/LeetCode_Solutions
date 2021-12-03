class Solution:
    def sortString(self, s: str) -> str:
        
        dict_ = dict(Counter(s))
        keys = sorted(dict_)
        
        res = []
        
        while len(res) != len(s):
            updated_dict = dict_.copy()
            
            for key in keys: #step 1, 2
                if updated_dict[key] != 0:
                    res.append(key)
                    updated_dict[key] -= 1
                    
            dict_ = updated_dict.copy()
            
            for key in keys[::-1]:
                if updated_dict[key] != 0:
                    res.append(key)
                    updated_dict[key] -= 1
                    
            dict_ = updated_dict.copy()
            
        return ''.join(res)