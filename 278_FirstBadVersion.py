# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        start=0
        end=n
        i=int((start+end)/2)
        while(True):
            if(isBadVersion(i)):
                if(isBadVersion(i-1)==False):
                    return i
                start,end=start,i-1
            else:
                start,end=i+1,end
            i=int((start+end)/2)
        """
        :type n: int
        :rtype: int
        """
