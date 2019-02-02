class Solution(object):
    def rob(self, nums):
        if not nums:
            return 0
        output=0
        cache=[0]*len(nums)
        if (len(nums)<3):
            return max(nums)
        cache[-1]=nums[-1]
        cache[-2]=nums[-2]
        cache[-3]=nums[-3]+nums[-1]
        if len(nums)==3:
            return max(cache)
        for i in reversed(range(len(nums)-3)):
            cache[i]=nums[i]+max(cache[i+2],cache[i+3])
        return max(cache)
        """
        :type nums: List[int]
        :rtype: int
        """
        
        
        
        """
        
        
