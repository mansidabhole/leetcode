class Solution(object):
    def plusOne(self, digits):
        if not digits:
            return
        if len(digits)==1:
            if digits[0]==9:
                output=[1,0]
                return output
            else:
                output=[digits[0]+1]
                return output
        from collections import deque
        output=deque()
        carry=0
        if digits[-1]+1 > 9:
            carry=1
            output.append(0)
        else:
            output.append(digits[-1]+1)
        for i in range(len(digits)-2,0,-1):
            if digits[i]+carry>9:
                carry=1
                output.appendleft(0)
            else:
                output.appendleft(digits[i]+carry)
                carry=0
        if digits[0]+carry>9:
            output.extendleft([0,1])
        else:
            output.appendleft(digits[0]+carry)
        return list(output)
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        