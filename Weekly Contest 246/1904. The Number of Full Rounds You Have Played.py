class Solution(object):
    def numberOfRounds(self, startTime, finishTime):
        """
        :type startTime: str
        :type finishTime: str
        :rtype: int
        """
        
        hs, ms = map(int, startTime.split(':'))
        hf, mf = map(int, finishTime.split(':'))
        
        next_day_bool = hs*60+ms > hf*60+mf #if true, then next day exist
        
        if hs*60+ms > hf*60+mf : #if got next day, increment finished hour by 24
            hf += 24
        
        #rounding up starting mins to nearest match start time.
        if ms> 0 and ms<=15:
            ms = 15
        elif ms>15 and ms<=30:
            ms = 30
        elif ms>30 and ms<=45:
            ms = 45
        elif ms>45 and ms<=60:
            ms = 0
            #increment hour 
            hs = hs+1
        else:
            print('Error in converting starting time.')
        
        #rounding down starting mins to nearest match finish time
        if mf >= 0 and mf<15:
            mf = 0
        elif mf>=15 and mf<30:
            mf = 15
        elif mf>=30 and mf<45:
            mf = 30
        elif mf>=45 and mf<60:
            mf = 45
        else:
            print('Error in converting finish time.')
            
        #if next day not exist and it exist after increment, means error.
        if not next_day_bool and hs*60+ms > hf*60+mf: 
            return 0
            
        started_time_per_round = (hs*60 + ms)//15
        finished_time_per_round = (hf*60 + mf)//15
        
        diff = finished_time_per_round - started_time_per_round
        
        return diff
            
        
        
        
        