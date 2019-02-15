class Solution(object):
    def coinChange(self, coins, amount):
        if not coins:
            return -1
        coins.sort()
        result=[[amount+5 for i in range(amount+1)]for j in range(len(coins))]
        for i in range(len(coins)):       #setting first column(for amount 0 to be zero)
            result[i][0]=0 
        for j in range(1,amount+1):         #filling out the first row
            if (j%coins[0]==0):
                result[0][j] = j/coins[0]             
        for i in range(1,len(coins)):
            for j in range(1,amount+1):
                if j>=coins[i]:
                    result[i][j]=min(result[i-1][j],result[i][j-coins[i]]+1)
                else:
                    result[i][j]=result[i-1][j]
        if result[-1][-1]==amount+5:
            return -1
        else:
            return result[-1][-1]
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        