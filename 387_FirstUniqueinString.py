class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        answer=dict()
        for i,ele in enumerate(s):
            if ele in answer.keys():
                answer[ele]=-2
            else:
                answer[ele]=i
        m=len(s)
        flag=0
        for key,value in answer.items():
            if value!= -2 and value<m:
                flag=1
                m=value
        if flag==1:
            return m
        else:
            return -1
                -