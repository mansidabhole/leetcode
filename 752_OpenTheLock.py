class Solution:
    def openLock(self, deadends, target):
        count=0
        string=''
        dummy=''
        hold=[]
        visited=set()
        dead=set(deadends)
        visited.add('0000')
        from collections import deque
        q=deque()
        if '0000' in deadends:
            return -1
        q.append(('0000',0))
        while(len(q)>0):
            string,val=q.popleft()
            for i in range(4):
                dummy=string[0:i]+str((int(string[i])+1)%10)+string[i+1:]
                if dummy not in visited:
                    hold.append(dummy)
                    visited.add(dummy)
                dummy=string[0:i]+str((int(string[i])-1)%10)+string[i+1:]
                if dummy not in visited:
                    hold.append(dummy) 
                    visited.add(dummy)
            for i in range(len(hold)):
                if hold[i] not in dead:
                    if hold[i]==target:
                        return val+1
                    q.append((hold[i],val+1))
            hold=[]
        return -1
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        