#Reference: https://leetcode.com/problems/making-file-names-unique/discuss/697825/Python-ACCEPTED-SOLUTION-with-dictionary-(hashmap)-and-set

class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        
        seen = set()
        ans = []
        dict_map = defaultdict(int)
        
        for name in names:
            
            freq = dict_map[name]
            new_name = name
            
            while new_name in seen:
                freq+=1
                new_name = name + '(' + str(freq) + ')'

            dict_map[name] = freq
                
            seen.add(new_name)
            ans.append(new_name)
           
        
        return ans
                