class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dict1=dict()
        dict2=dict()
        answer=[]
        for ele in nums1:
            if ele in dict1.keys():
                dict1[ele]+=1
            else:
                dict1[ele]=1
        for ele in nums2:
            dict2[ele]=0
        for ele in nums2:
            if ele in dict1.keys():
                if dict1[ele]!=0:
                    dict2[ele]+=1
                    dict1[ele]-=1
        for key,value in dict2.items():
            while value!=0:
                answer.append(key)
                value-=1
        return answer