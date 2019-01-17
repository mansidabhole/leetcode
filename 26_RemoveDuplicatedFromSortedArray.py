 class Solution:
    def removeDuplicates(self, nums):
        temp=0
        i=1
        while(i<len(nums)):
            if(nums[i]>nums[temp]):
                temp+=1
                i+=1
            else:
                del nums[i]
        return len(nums)
        """
        :type nums: List[int]
        :rtype: int
        """