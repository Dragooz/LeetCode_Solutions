#Reference: https://leetcode.com/problems/rank-teams-by-votes/discuss/524869/C%2B%2BPython-Count-Votes

class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        
        count = {v: [0] * len(votes[0]) + [v] for v in votes[0]} #if len==3, then it will be like {A: [0, 0, 0, 'A']}
        
        for vote in votes:
            for i, v in enumerate(vote):
                count[v][i] -= 1
        
        sort_ = sorted(votes[0], key=count.get) #sort from first val in count first, then follow by second and third and on and on
        
        return ''.join(sort_)
        
        