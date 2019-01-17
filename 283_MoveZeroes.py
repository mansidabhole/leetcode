
class Solution:
    def moveZeroes(self, nums):
        i=0
        count=0
        l=len(nums)
        while(i<l and l>1):
            if(nums[i]==0):
                del nums[i]
                count+=1
                nums.append(0)
                l-=1
            else:
                i+=1      
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """