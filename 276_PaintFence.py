class Solution(object):
    def numWays(self, n, k):
        if not k or not n:
            return 0
        if n==1:
            return k
        same=[]
        diff=[]
        same.append(0)
        diff.append(k)
        same.append(k)
        diff.append((k-1)*k)
        for i in range(2,n):
            same.append(diff[i-1])
            diff.append((k-1)*same[i-1]+(k-1)*diff[i-1])
        return (same[-1]+diff[-1]) 
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        