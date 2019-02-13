class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1)>len(nums2):
            nums1,nums2=nums2,nums1
        m=len(nums1)
        n=len(nums2)
        tmed=0
        start=0
        end=len(nums1)
        median=(len(nums1)+len(nums2)+1)/2
        while(start<=end):
            p1=(start+end)/2
            p2=median-p1
            if (p1>0 and p2<n and nums1[p1-1]>nums2[p2]):   #check valid conditions and shiftleft
                end=p1-1
            elif(p1<m and p2>0 and nums2[p2-1]>nums1[p1]):
                start=p1+1
            else:
                if p1==0:
                    tmed=nums2[p2-1]
                elif p2==0:
                    tmed=nums1[p1-1]
                else:
                    tmed=max(nums1[p1-1],nums2[p2-1])
                break
        if (n+m)%2==1:
            return tmed
        else:
            if p1==m:
                return (tmed+nums2[p2])/2.0
            elif p2==n:
                return (tmed+nums1[p1])/2.0
            else:
                return (tmed+min(nums1[p1],nums2[p2]))/2.0           
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        