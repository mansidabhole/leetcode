class Solution:
    def dailyTemperatures(self, T):
        if not T:
            return
        output=['']*len(T)
        stack=[]
        for i,ele in enumerate(T):
            while(len(stack)>0):
                if ele>stack[-1][0]:
                    n,val=stack.pop()
                    output[val]=i-val
                    continue
                break
            stack.append((ele,i))
        while(len(stack)>0):
            n,val=stack.pop()
            output[val]=0
        return output
        """
        :type T: List[int]
        :rtype: List[int]
        """
        