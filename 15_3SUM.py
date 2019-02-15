class Solution(object):
    def threeSum(self, nums):
        if not nums:
            return []
        if len(set(nums))==1 and nums[0]==0 and len(nums)>2:
            return [[0,0,0]]
        output=[]
        target=0
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i]==nums[i-1]:
                continue
            target=nums[i]*(-1)
            s,e=i+1,len(nums)-1
            while(s<e):
                if (nums[s]+nums[e])==target:
                    output.append([nums[i],nums[s],nums[e]])
                    s+=1
                    while s<e and nums[s]==nums[s-1]:
                            s+=1
                elif nums[s]+nums[e]<target:
                    s+=1
                else:
                    e-=1
        return output
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        