class Solution:
    def groupAnagrams(self, strs):
        output={}
        for ele in strs:
            key=tuple(sorted(ele))
            output.setdefault(key,[]).append(ele)
        return list(output.values())     
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """