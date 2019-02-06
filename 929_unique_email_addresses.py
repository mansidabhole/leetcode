class Solution:
    def numUniqueEmails(self, emails: 'List[str]') -> 'int':
        count=0
        cache=dict()
        for i in range(len(emails)):
            addr=emails[i]
            pos=addr.find('@')
            local=addr[:pos]
            domain=addr[pos+1:]
            plus=local.find('+')
            if plus != -1:
                local=local[:plus]
            dot=local.find('.')    
            while (dot != -1):
                local=local[:dot]+local[dot+1:]
                dot=local.find('.')
            if local not in cache.keys():
                cache[local]=1
                cache[domain]=1
                count+=1
                continue
            if domain not in cache.keys():
                cache[domain]=1
                count+=1
        return count