class Solution(object):
    def wordBreak(self, s, wordDict):
        cache=[[False for i in range(len(s))]for j in range(len(s))]
        for i in range(len(s)-1,-1,-1):
            for j in range(i,len(s)):
                if s[i:j+1] in wordDict:
                    cache[i][j]=True
                else:
                    for k in range(i,j+1):
                        if (cache[i][k]==True and cache[k+1][j]==True):
                            cache[i][j]=True
                            break
        return cache[0][len(s)-1]
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        