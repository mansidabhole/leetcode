class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0
        count=0
        string='1'
        from collections import deque
        d=deque()
        numrows,numcols=len(grid),len(grid[0])
        for m in range(numrows):
            for n in range(numcols):
                if (grid[m][n]=='1'):
                    d.append((m,n))
                    grid[m][n]='#'
                    while(len(d)>0):
                        i,j=d.popleft()
                        if ((i-1)>=0 and  grid[i-1][j]==string):
                            d.append((i-1,j))
                            grid[i-1][j]='#'
                        if ((i+1)<numrows and grid[i+1][j]==string):
                            d.append((i+1,j))
                            grid[i+1][j]='#'
                        if ((j-1)>=0 and  grid[i][j-1]==string):
                            d.append((i,j-1))  
                            grid[i][j-1]='#'
                        if ((j+1)<numcols and grid[i][j+1]==string):
                            d.append((i,j+1))
                            grid[i][j+1]='#'
                    count+=1
        return count          
        """
        :type grid: List[List[str]]
        :rtype: int
        """