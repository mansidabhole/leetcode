class Solution(object):
    def generateParenthesis(self, n):
        res=[]
        def backtrack(s,left,right):
            if len(s)==2*n:
                res.append(s)
            if left<n:
                backtrack(s+"(",left+1,right)
            if right<left:
                backtrack(s+")",left,right+1)
        backtrack("",0,0)
        return res
        """
        :type n: int
        :rtype: List[str]
        """
        
        
        """
        solution 1:
         def embed(string):
            res=set()
            for i,ele in enumerate(string):
                if ele==')':
                    res.add(str(string[0:i]+'()'+string[i:]))
            res.add(str(str(string)+'()'))
            res.add(str('()'+str(string)))
            return res
        if n==0:
            return []
        if n==1:
            return ['()']
        prev=set()
        prev=embed('()')
        for i in range(2,n):
            prev=[j for new in prev for j in embed(new)]
        return list(set(prev))
        """