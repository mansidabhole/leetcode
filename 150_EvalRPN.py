class Solution:
    def evalRPN(self, tokens):
        if not tokens:
            return 0
        operators={'+': lambda y, x: y + x,
                   '-': lambda y, x: x - y,
                   '*': lambda y, x: x * y, 
                   '/': lambda y, x: int(operator.truediv(x,y))
                  }
        stack=[]
        for i in tokens:
            if i in operators.keys():
                stack.append(operators[i](int(stack.pop()),int(stack.pop())))
            else:
                stack.append(i)
        return int(stack[-1])
        """
        :type tokens: List[str]
        :rtype: int
        """
        