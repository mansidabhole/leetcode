class Solution:
    def convert(self, s: 'str', numRows: 'int') -> 'str':
        if numRows==1:
            return s
        zigzag=["" for i in range(numRows)]
        row=0
        i=0
        ans=""
        while(True):
            while(row<numRows and i<len(s)):
                zigzag[row]+=s[i]
                i+=1
                row+=1
            row-=2
            while(row>=0 and i<len(s)):
                zigzag[row]+=(s[i])
                row-=1
                i+=1
            row=1
            if i==len(s):
                break
        return ''.join(zigzag)
            
        