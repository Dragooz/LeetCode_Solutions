class Solution:
    def maximumTime(self, time: str) -> str:
        
        time = time.split(':')
        ans = ''
        for index, t in enumerate(time):
            if index == 0:
                if t[0] == '?' and t[1] == '?':
                    ans += '23:'
                elif t[0] =='?' and t[1] != '?':
                    if int(t[1]) >= 4:
                        ans += '1' + t[1] + ':'
                    else:
                        ans += '2' + t[1] + ':'
                elif t[0] != '?' and t[1] == '?':
                    if int(t[0]) <= 1:
                        ans += t[0] + '9:'
                    else:
                        ans += t[0] + '3:'
                else:
                    ans += t[:2] + ':'
            else:
                if t[0] == '?' and t[1] == '?':
                    ans += '59'
                elif t[0] =='?' and t[1] != '?':
                    ans += '5' + t[1]
                elif t[0] != '?' and t[1] == '?':
                        ans += t[0] + '9'
                else:
                    ans += t[:2]
                    
        return ans