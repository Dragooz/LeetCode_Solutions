class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        
        def extract_date(date):
            return int(date[0:4]), int(date[5:7]), int(date[8:]) #year, month, day
        
        y1, m1, d1 = extract_date(date1)
        y2, m2, d2 = extract_date(date2)
        
        return abs((datetime.datetime(y2, m2, d2) - datetime.datetime(y1, m1, d1)).days)