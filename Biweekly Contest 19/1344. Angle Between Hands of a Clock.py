class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        
        #1 tick = 6 deg
        #for minute, the degree is 6*minute
        #for hour, the degree is initial +/- 30 deg / minute
        
        md = minutes*6
        hd = (hour%12)*30 + ((30/60) * minutes)

        return min(abs(hd-md), 360-abs(hd-md))
        
        
        
        
        
        