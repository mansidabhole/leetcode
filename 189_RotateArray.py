
class Solution:
    def rotate(self, nums, k):
        if k<=0 or len(nums)==1:
            return
        k=k%len(nums)
        end=len(nums)-1
        self.reverse(nums,0,end-k)
        self.reverse(nums,end-k+1,end)
        self.reverse(nums,0,end)
    def reverse(self,nums,start,end):
        while(start<end):
            nums[start],nums[end]=nums[end],nums[start]
            start,end=start+1,end-1
        return
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        """
        solution 1 : with space O(nums)
        
        l=len(nums)
        temp=nums[:]
        for i in range(len(nums)):
            temp[(i+k)%l]=nums[i]
        nums[0:l]=temp[0:l]
        
        
        
        solution 2: space=O(1) but TLE
         while(k>0):
            temp=nums[-1]
            for i in reversed(range(1,len(nums))):
                nums[i]=nums[i-1]
            nums[0]=temp
        """
