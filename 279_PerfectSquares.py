class Solution:
    def numSquares(self, n):
        from collections import deque
        q=deque()
        visited=set()
        visited.add(n)
        q.append((n,0))
        while(len(q)>0):
            num,val=q.popleft()
            m=math.floor(math.sqrt(num))
            for i in range(m+1):
                if num-(i**2)==0:
                    return val+1
                if num-(i**2) not in visited:
                    q.append((num-i**2,val+1))
                    visited.add(num-i**2)
        return -1
        """
        :type n: int
        :rtype: int
        """
        