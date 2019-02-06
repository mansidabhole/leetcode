class Solution:
    def longestPalindrome(self, s):
        self.cache=[[0 for x in range(len(s))]for y in range(len(s))]
        start=0
        max_len=1
        for i in range(len(s)):       #single characters are palindromes
            self.cache[i][i]=True
        for i in range(len(s)-1):      #2 letter palindromes 
            if s[i]==s[i+1]:
                self.cache[i][i+1]=True
                start=i
                max_len=2
            else:
                self.cache[i][i+1]=False
        k=3
        while(k<=len(s)):
            for i in range(len(s)-k+1):
                j=i+k-1
                if s[i]==s[j]:
                    if self.cache[i+1][j-1]==True:
                        self.cache[i][j]=True
                        if k>max_len:
                            max_len=k
                            start=i
                    else:
                        self.cache[i][j]=False
                else:
                    self.cache[i][j]=False
            k+=1
        return s[start:start+max_len]
            
        