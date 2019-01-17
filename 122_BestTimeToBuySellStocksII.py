class Solution:
    def maxProfit(self, prices):
        total=0
        i=len(prices)-1
        while(i>0):
            if prices[i-1]<prices[i]:
                total+=(prices[i]-prices[i-1])
            i-=1
        return total
        """
        :type prices: List[int]
        :rtype: int
        """