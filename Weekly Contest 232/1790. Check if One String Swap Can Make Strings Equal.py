class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        ans = []
        for index, (a, b) in enumerate (zip(s1, s2)):
            if a != b:
                ans.append(index)
                
        if len(ans) == 0:
            return True
        elif len(ans) == 2:
            if s1[ans[0]] == s2 [ans[1]] and s1[ans[1]] == s2[ans[0]]:
                return True
            else:
                return False
        else:
            return False