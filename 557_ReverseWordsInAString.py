class Solution:
    def reverseWords(self, s: 'str') -> 'str':
        reverse=""
        pos=s.find(' ')
        if pos==-1:
            return s[::-1]
        while(pos!=-1):  
            word,s=s[:pos],s[pos+1:]
            reverse+=(word[::-1]+' ')
            pos=s.find(' ')
        reverse+=s[::-1]
        return reverse
 