class Solution:
    def reverseString(self, s):
        output=''
        for i in reversed(range(len(s))):
            output+=s[i]
        return output
        """
        :type s: str
        :rtype: str
        """
        """
        solution 1: memory limit exceeded
         if (len(s)==0):
            return s
        c1=s[0]
        c2=s[-1]
        s=c2+s[1:]
        s=s[:-1]+c1
        start=1
        end=len(s)-2
        while(start<end):
            c1=s[start]
            c2=s[end]
            s=s[:start]+c2+s[start+1:]
            s=s[:end]+c1+s[end+1:]
            start,end=start+1,end-1
        return s
        """