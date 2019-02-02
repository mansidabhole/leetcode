class Solution(object):
    def maxSubArray(self, nums):
        if not nums:
            return 
        output=nums[-1]
        prev=nums[-1]
        for i in reversed(range(len(nums)-1)):
            prev=max(nums[i]+prev,nums[i])
            output=max(prev,output)
        return output
        """
        :type nums: List[int]
        :rtype: int
        """nt
        """
        
        
        
        """
        
        
