cclass Solution:
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        count=0
        s=[]
        t=[]
        if len(intervals)==0:
            return 0
        for i in range(len(intervals)):
            s.append(intervals[i].start)
            t.append(intervals[i].end)
        s=sorted(s)
        t=sorted(t)
        j=1
        min_val=t[0]
        for i in range(len(intervals)):
            if t[i]<=min_val:
                t[i]=min_val
            if s[i]>=min_val:
                min_val=t[j]
                j=j+1
            else:
                count+=1
        return count