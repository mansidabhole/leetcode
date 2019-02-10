class Solution(object):
    def sortArrayByParity(self, A):
        ans=[]
        for i in range(len(A)):
            if A[i]%2==0:
                ans.append(A[i])
                A[i]=-1
        for i in range(len(A)):
            if A[i]!=-1:
                ans.append(A[i])
        return ans        
        """
        :type A: List[int]
        :rtype: List[int]
        """
        