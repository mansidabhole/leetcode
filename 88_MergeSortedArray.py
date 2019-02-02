class Solution(object):
    def merge(self, nums1, m, nums2, n):
        nums1_copy=[]
        nums1_copy[:]=nums1[:m]
        i,j=0,0
        for k in range(m+n):
            if i<m and j<n:
                if nums1_copy[i]<=nums2[j]:
                    nums1[k]=nums1_copy[i]
                    i+=1
                else:
                    nums1[k]=nums2[j]
                    j+=1
            elif i>=m:
                nums1[k]=nums2[j]
                j+=1
            else:
                nums1[k]=nums1_copy[i]
                i+=1
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        
        
        
