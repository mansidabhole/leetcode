class MovingAverage:

    def __init__(self, size):
        self.q=[]
        self.size=size
        self.count=0
        self.j=0
        """
        Initialize your data structure here.
        :type size: int
        """
        

    def next(self, val):
        if(self.count>=self.size):
            self.j+=1
            self.count-=1
        else:
            self.j=0
        self.q.append(val)
        self.count+=1
        upper=self.count+self.j
        return float(sum(self.q[i] for i in range(self.j,upper))/self.count)