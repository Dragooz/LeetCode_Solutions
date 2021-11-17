class Solution:
    def maxDiff(self, num: int) -> int:
        
        fn_replace = -1
        sn_replace = -1
        
        f_num = s_num = num
        
        for i in range(len(str(num))):
            if str(num)[i] != '9':
                f_num = (str(f_num)).replace(str(num)[i], '9')
                break
                
        if str(num)[0] != '1':
            s_num = (str(s_num)).replace(str(num)[0], '1')
        else:
            for i in range(1, len(str(num))):
                if str(num)[i] != '0' and str(num)[i]!= '1':
                    s_num = (str(s_num)[1:]).replace(str(num)[i], '0')
                    s_num = '1' + s_num
                    break
        
        print(f_num), print(s_num)
        
        return int(f_num) - int(s_num)
                
        
        
        
            
        
            
            