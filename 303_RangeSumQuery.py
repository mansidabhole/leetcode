class NumArray(object):

    def __init__(self, nums):
        self.size=len(nums)
        if nums:          
            self.cache=[]
            self.cache.append(nums[-1])
            for ele in reversed(nums[:-1]):
                self.cache.append(self.cache[-1]+ele)          
        """
        :type nums: List[int]
        """
    

    def sumRange(self, i, j):
        if self.size==0:
            return 0
        if j!=self.size-1:
            return (self.cache[-(i+1)]-self.cache[-(j+2)])
        else:
            return(self.cache[-(i+1)])
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        
        
