class Solution:
    def isPalindrome(self, s):
        s=s.lower()
        dummy=''
        i=len(s)-1
        while(i>=0):
            if(s[i].isalnum()):
                dummy=dummy[0:]+s[i]
            else:
                s=s[0:i]+s[i+1:]
            i-=1
        return(dummy==s)
        """
        :type s: str
        :rtype: bool
        """
        