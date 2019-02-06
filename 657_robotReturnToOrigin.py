class Solution:
    def judgeCircle(self, moves: 'str') -> 'bool':
        c=collections.Counter(moves)
        return c['L']==c['R'] and c['U']==c['D']
        
        
        
        
        
        
        
        
#solution 1
"""
cache={'R':(1,0),'L':(-1,0),'U':(0,1),'D':(0,-1)}
        x,y=0,0
        if not moves:
            return True
        for c in moves:
            x+=[t for t in cache[c]][0]
            y+=[t for t in cache[c]][1]
        if x==0 and y==0:
            return True
        else:
            return False
"""
 