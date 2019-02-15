class Solution(object):
    def productExceptSelf(self, nums):
        output=[0]*len(nums)
        productl=[0]*len(nums)
        output[-1]=1
        for i in range(len(nums)-2,-1,-1):
            output[i]=nums[i+1]*output[i+1]
        productl[0]=1
        for i in range(1,len(nums)):
            productl[i]=productl[i-1]*nums[i-1]
        for i in range(0,len(nums)):
            output[i]=output[i]*productl[i]
        return output
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        