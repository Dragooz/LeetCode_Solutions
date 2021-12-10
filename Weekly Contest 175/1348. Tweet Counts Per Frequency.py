#https://leetcode.com/problems/tweet-counts-per-frequency/discuss/503447/Python-binary-search

class TweetCounts:

    def __init__(self):
        self.t = defaultdict(list)

    def recordTweet(self, tweetName: str, time: int) -> None:
        bisect.insort(self.t[tweetName], time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        time = 0
        if freq == 'minute':
            time = 60
        elif freq == 'hour':
            time = 3600
        elif freq == 'day':
            time = 86400
        
        i = startTime
        
        ans = []
        while i <= endTime:
            j = min(i+time, endTime+1)
            tweet_num = bisect.bisect_left(self.t[tweetName], j) - bisect.bisect_left(self.t[tweetName], i) #bisect left because its [0,59]
            ans.append(tweet_num)
            i+=time
            
        return ans


# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)