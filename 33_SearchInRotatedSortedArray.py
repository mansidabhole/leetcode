class Solution(object):
    def search(self, nums, target):
        def searchIndex(start,end):     #fxn to search for the rotate index(smallest element)
            if nums[start]<nums[end]:
                return 0
            while(start<=end):
                t=(start+end)/2
                if nums[t]>nums[t+1]:
                    return t+1
                elif nums[t]<nums[start]:
                    end=t-1
                else:
                    start=t+1
        def binarysearch(start,end):   #fxn to perform binary search
            while(start<=end):
                t=(start+end)/2
                if nums[t]==target:
                    return t
                elif nums[t]<target:
                    start=t+1
                else:
                    end=t-1
            return -1
        if not nums:
            return -1
        l=len(nums)
        if l==1:
            if nums[0]==target:
                return 0
            else:
                return -1
        rindex=0
        rindex=searchIndex(0,l-1)
        if target==nums[0]:
            return 0
        if target==nums[rindex]:
            return rindex
        if rindex==0:          #case where array is not rotated
            res=binarysearch(0,l-1)
        elif target<nums[0]:
            res=binarysearch(rindex+1,l-1)
        else:
            res=binarysearch(0,rindex-1)
        return res
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """