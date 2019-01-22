class Solution:
    def isValid(self, s):
        if not s:
            return True
        valid={'{}','()','[]'}
        from collections import deque
        q=deque()
        for i in s:
            if i=='{' or i=='(' or i=='[':
                q.append(i)
            elif len(q)>0:
                    c=q.pop()
                    if c+i not in valid:
                        return False
            else:
                return False
        if (len(q)==0):
            return True
        return False
        """
        :type s: str
        :rtype: bool
        """