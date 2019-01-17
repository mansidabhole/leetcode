 class Solution:
    def isAnagram(self, s, t):
        d1={}
        d2={}
        for i in s:
            z=d1.setdefault(i,0)
            z+=1
            d1[i]=z
        for i in t:
            z=d2.setdefault(i,0)
            z+=1    
            d2[i]=z
        if(d1==d2):
            return True
        return False
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        """
        solution 1: 
        if(sorted(s)==sorted(t)):
            return True
        return False
        
        """