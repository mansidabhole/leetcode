class Solution:
    def maxProfit(self, prices):
        if len(prices)!=0:
            high=prices[-1]
            temp=[0]*len(prices)
            for i in reversed(list(range(0,len(prices)-1))):
                temp[i]=high-prices[i]
                if prices[i]>high:
                    high=prices[i]  
            temp=sorted(temp)
            return temp[-1]
        else:
            return 0
        """
        :type prices: List[int]
        :rtype: int
        """