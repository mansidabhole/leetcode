class Solution:
    def wallsAndGates(self, rooms):
        if not rooms:
            return
        from collections import deque
        d=deque()
        numrows=len(rooms)
        numcols=len(rooms[0])
        for m in range(numrows):
            for n in range(numcols):
                if rooms[m][n]==0:
                    d.append((m,n,0))
                    visited=[]
                    while(len(d)>0):
                        i,j,val=d[0]
                        if i!=0:
                            if (rooms[i-1][j]!=0 and rooms[i-1][j]!=-1 and ((i-1,j) not in visited)):
                                d.append((i-1,j,val+1))
                                visited.append((i-1,j))
                                if (val+1)<rooms[i-1][j]:
                                    rooms[i-1][j]=val+1
                        if j!=0:
                            if (rooms[i][j-1]!=0 and rooms[i][j-1]!=-1 and ((i,j-1) not in visited)):
                                d.append((i,j-1,val+1))
                                visited.append((i,j-1))
                                if  (val+1)<rooms[i][j-1]:
                                    rooms[i][j-1]=val+1
                        if i!=(numrows-1):
                            if (rooms[i+1][j]!=0 and rooms[i+1][j]!=-1 and ((i+1,j) not in visited)):
                                d.append((i+1,j,val+1))
                                visited.append((i+1,j))
                                if (val+1)<rooms[i+1][j]:
                                    rooms[i+1][j]=val+1
                        if j!=(numcols-1):
                            if (rooms[i][j+1]!=0 and rooms[i][j+1]!=-1 and ((i,j+1) not in visited)):
                                d.append((i,j+1,val+1))
                                visited.append((i,j+1))
                                if (val+1)<rooms[i][j+1]:
                                    rooms[i][j+1]=val+1
                        d.popleft()
                                
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        