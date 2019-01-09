class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        output=[]
        nums1=set(nums1)
        nums2=set(nums2)
        for i in nums2:
            if i in nums1:
                output.append(i)
        return output
            