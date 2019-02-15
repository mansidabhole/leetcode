## Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        if not intervals:
            return []
        intervals.sort(key=lambda x: x.start)
        res=[]
        res.append(intervals[0])
        i=0
        while(i<len(intervals)-1):
            if res[-1].end>=intervals[i+1].start:
                res[-1].end=max(intervals[i+1].end,res[-1].end)
            else:
                res.append(intervals[i+1])
            i+=1
        return res                   
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        
        
        