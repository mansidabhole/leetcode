class Solution(object):
    def totalFruit(self, tree):
        cache=dict()
        output=0
        i=0
        for j,ele in enumerate(tree):     #slidingwindow
            cache[ele]=cache.setdefault(ele,0)+1
            while(len(cache)>2):
                cache[tree[i]]-=1
                if cache[tree[i]]==0:
                    del cache[tree[i]]
                i+=1
            output=max(output,j-i+1)
        return output
        """
        :type tree: List[int]
        :rtype: int
        """
        
        