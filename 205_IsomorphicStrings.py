class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        iso=dict()
        for i,j in zip(s,t):
            if i in iso.keys():
                if iso[i]!=j:
                    return False
            elif j in iso.values():
                return False
            else:
                iso[i]=j
        return True
                