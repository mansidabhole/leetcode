class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        l=len(nums)
        if l==1:
            return nums[0]
        i=0
        while(True):
            if nums[i] != nums[i+1]:
                return nums[i]
            i=i+2
            if i==len(nums)-1:
                break
        return nums[l-1]
            