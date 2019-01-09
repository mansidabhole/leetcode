class Solution:
    def groupStrings(self, strings):
        output={}
        for ele in strings:
            s=''
            if len(ele)==1:
                t='z'
            else:
                m= ord(ele[0])-97
                for i in range(len(ele)):
                    if (ord(ele[i])-m < 97):
                        s=s+chr((ord(ele[i])-m)+26)
                    else:
                        s=s+chr((ord(ele[i])-m))
            output.setdefault(s,[]).append(ele)
        return list(output.values())
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """