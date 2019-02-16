class Solution(object):
    def numDecodings(self, s):
        #using memoization and dynamic programming
        memo=[-1]*(len(s)+1)
        def countways(s,k):
            if k==0:
                memo[k]=1
                return 1
            start=len(s)-k
            if int(s[start])==0:
                memo[k]=0
                return 0
            if memo[k]!=-1:
                return memo[k]
            res=countways(s,k-1)
            if int(s[start:start+2])<27 and k>=2:
                res+=countways(s,k-2)
            memo[k]=res
            return res
        if not s:
            return 0
        countways(s,len(s))
        return memo[-1]
        """
        :type s: str
        :rtype: int
        """
        