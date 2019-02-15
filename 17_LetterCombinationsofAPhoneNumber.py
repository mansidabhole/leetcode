class Solution(object):
    def letterCombinations(self, digits):
        mappings={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        result=[]
        if not digits:
            return result
        if len(digits)==1:
            return list(mappings[digits[0]])
        last=list(mappings[digits[-1]])
        prev=self.letterCombinations(digits[0:-1])
        result=[p+l for p in prev for l in last] 
        return result
        """
        :type digits: str
        :rtype: List[str]
        """
        
        