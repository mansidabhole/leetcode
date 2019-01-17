 class Solution:
    def reverse(self, x):
        flag=0
        if x<0:
            x=-(x)
            flag=1
        temp=[int(i) for i in str(x)]
        temp.reverse()
        output=''.join(map(str,temp))
        output=int(output)
        if flag==1:
            output=-(output)
        if output+1 > 2**31:
            return 0
        elif -(output) > 2**31:
            return 0
        else:
            return output
        """
        :type x: int
        :rtype: int
        """