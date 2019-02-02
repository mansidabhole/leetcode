class Solution(object):
    def minCostClimbingStairs(self, cost):
        if len(cost)==2:
            return min(cost)
        opt1=0
        opt2=min(cost[1],cost[0])
        for i in range(3,len(cost)+1):
            t= min((cost[i-1]+opt2),(cost[i-2]+opt1))
            opt1,opt2=opt2,t
        return t
        """
        :type cost: List[int]
        :rtype: int
        """
        
        
        """
        
        
