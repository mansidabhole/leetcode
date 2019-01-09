class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        duplicate=dict()
        for i,ele in enumerate(nums):
            if ele in duplicate.keys():
                if abs(duplicate[ele]-i)<=k:
                    return True
                else:
                    duplicate[ele]=i
            else:
                duplicate[ele]=i
        return False